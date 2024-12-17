import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

import click

from .db import get_db

auth = Blueprint('auth', __name__)


@auth.route("state", methods=["GET"])
def state():
    if session.get("logged") is None:
        return jsonify({"logged": "false"})
    else:
        return jsonify({"logged": "true"})


@auth.route("login", methods=["POST"])
def login():
    password = request.get_json().get("password")
    # state = False

    with open("server/instance/usr", "r") as pwd:
        verify = check_password_hash(pwd.read(), password)

    if verify:
        session.clear()
        session["logged"] = "true"
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error",
                        "message": "Wrong password"})


@click.command("set-password")
def set_password_command():
    # with open("./server/instance/auth/usr", "w") as pwd:
    #     pwd.write(generate_password_hash(input("Password: ")))

    with current_app.open_instance_resource("usr", "w") as f:
        f.write(generate_password_hash(input("Password: ")))

    click.echo("Password set.")


def init_app(app):
    app.cli.add_command(set_password_command)
