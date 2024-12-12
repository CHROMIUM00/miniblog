from flask import Flask, jsonify, Blueprint, request, session
from werkzeug.security import generate_password_hash, check_password_hash

from .db import get_db

user = Blueprint("user", __name__)


@user.route("login", methods=["POST"])
def login():
    user_data = request.get_json()
    db = get_db()
    dbuser = db.execute(
        "SELECT id, username, password"
        " FROM user"
        " WHERE username = ?",
        (user_data.get("username"),)
    ).fetchone()

    if dbuser is None:
        return jsonify({"status": "error", "message": "User not found"})
    elif not check_password_hash(dbuser["password"], user_data.get("password")):
        return jsonify({"status": "error", "message": "Wrong password"})

    session.clear()
    session["user_id"] = dbuser["id"]
    return jsonify({"status": "success"})
