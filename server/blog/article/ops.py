import os

from flask import Flask, jsonify, Blueprint, request

from ..db import get_db

post = Blueprint("post", __name__)


@post.route("getlist", methods=["GET"])
def getlist():
    db = get_db()
    response_object = {"status": "nihao"}

    dblist = db.execute(
        "SELECT type, remote_id"
        " FROM list"
        " ORDER BY id DESC"
    ).fetchall()  # try fetchmany()

    response_object["data"] = []
    for i in dblist:
        if i["type"] == "article":
            entry = db.execute(
                "SELECT id, title, description, created, author"
                " FROM post"
                " WHERE id = ?",
                (i["remote_id"],)
            ).fetchone()
            response_object["data"].append({
                "type": "article",
                "id": entry["id"],
                "title": entry["title"],
                "desc": entry["description"],
                "created": entry["created"].strftime('%Y-%m-%d %H:%M:%S'),
                "author": entry["author"],
            })
        elif i["type"] == "comment":
            entry = db.execute(
                "SELECT id, post_title, post_id,author, content, created"
                " FROM comment"
                " WHERE id = ?",
                (i["remote_id"],)
            ).fetchone()
            response_object["data"].append({
                "type": "comment",
                "id": entry["id"],
                "post_id": entry["post_id"],
                "post_title": entry["post_title"],
                "author": entry["author"],
                "content": entry["content"],
                "created": entry["created"].strftime('%Y-%m-%d %H:%M:%S'),
            })

    return jsonify(response_object)


@post.route("getpostlist", methods=["GET"])
def get_post_list():
    db = get_db()
    response_object = {"status": "nihao"}

    dbposts = db.execute(
        "SELECT p.id, title, description, created, author"
        " FROM post p"
    ).fetchall()

    response_object['data'] = []
    for p in dbposts:
        post_data = {
            "type": "article",
            "id": p["id"],
            "title": p["title"],
            "desc": p["description"],
            "created": p["created"].strftime('%Y-%m-%d %H:%M:%S'),
            "author": p["author"],
            "sorting": int(p["created"].timestamp())
        }
        response_object["data"].append(post_data)

    return jsonify(response_object)


@post.route("getcommentlist", methods=["GET"])
def get_comment_list():
    db = get_db()
    response_object = {"status": "nihao"}

    dbcomments = db.execute(
        "SELECT c.id, post_title, author, content, created"
        " FROM comment c"
    ).fetchall()

    response_object['data'] = []
    for c in dbcomments:
        comment_data = {
            "type": "comment",
            "id": c["id"],
            "post_title": c["post_title"],
            "author": c["author"],
            "content": c["content"],
            "created": c["created"].strftime('%Y-%m-%d %H:%M:%S'),
            "sorting": int(c["created"].timestamp())
        }
        response_object["data"].append(comment_data)

    return jsonify(response_object)


@post.route("getdetail/<int:id>", methods=["GET"])
def get_post(id):
    response_object = {"status": "nihao"}
    db = get_db()
    post = db.execute(
        "SELECT p.id, title, author, created, description"
        " FROM post p"
        " WHERE p.id = ?",
        (id,)
    ).fetchone()

    if post is None:
        return jsonify({"error": "Post not found"}), 404

    post_data = {
        "id": post["id"],
        "title": post["title"],
        "author": post["author"],
        "desc": post["description"],
        "created": post["created"].strftime('%Y-%m-%d %H:%M:%S')
    }
    with open(f"server/instance/articles/{id}", "r") as f:
        post_data["body"] = f.read()

    response_object["post"] = post_data

    return jsonify(response_object)


@post.route("getcomment/<int:postid>", methods=["GET"])
def get_comment(postid):
    response_object = {"status": "nihao"}
    db = get_db()

    dbcomments = db.execute(
        "SELECT c.id, content, author, created"
        " FROM comment c"
        " WHERE c.post_id = ?"
        " ORDER BY created DESC",
        (postid,)
    ).fetchall()

    response_object['comments'] = []
    for c in dbcomments:
        comment_data = {
            "id": c["id"],
            "content": c["content"],
            "author": c["author"],
            "created": c["created"].strftime('%Y-%m-%d %H:%M:%S')
        }
        response_object["comments"].append(comment_data)

    return jsonify(response_object)


@post.route("addcomment/<int:postid>", methods=["POST"])
def add_comment(postid):
    comment_data = request.get_json()
    db = get_db()
    cur = db.execute(
        "INSERT INTO comment (post_id, post_title, author, mail, content)"
        " VALUES (?, ?, ?, ?, ?)",
        (postid,
         comment_data.get("post_title"),
         comment_data.get("author"),
         comment_data.get("mail"),
         comment_data.get("body"),
         )
    )
    db.commit()

    comment_id = cur.lastrowid
    db.execute(
        "INSERT INTO list (type, remote_id)"
        " VALUES (?, ?)",
        ("comment", comment_id)
    )
    db.commit()

    return jsonify({"status": "nihao"})


@post.route("create", methods=["POST"])
def create():
    article = request.get_json()
    db = get_db()
    cur = db.execute(
        "INSERT INTO post (title, author, description)"
        " VALUES (?, ?, ?)",
        (article.get("title"),
         article.get("author"),
         article.get("desc"),
         )
    )
    db.commit()

    article_id = cur.lastrowid
    print(article_id)
    print(f"{article_id}")
    with open(f"server/instance/articles/{article_id}", "w") as f:
        f.write(article.get("body"))

    db.execute(
        "INSERT INTO list (type, remote_id)"
        " VALUES (?, ?)",
        ("article", article_id)
    )
    db.commit()

    return jsonify({"status": "success"})


@post.route("update/<int:id>", methods=["POST"])
def update(id):
    updated = request.get_json()
    db = get_db()
    db.execute(
        "UPDATE post"
        " SET title = ?, created = CURRENT_TIMESTAMP, author = ?, description = ?"
        " WHERE id = ?",
        (updated.get("title"),
         updated.get("author"),
         updated.get("desc"),
         id,
         )
    )
    db.commit()

    with open(f"server/instance/articles/{id}", "w") as f:
        f.write(updated.get("body"))

    return jsonify({"status": "success"})


@post.route("delete/<int:id>", methods=["POST"])
def delete(id):
    db = get_db()
    db.execute(
        "DELETE FROM post"
        " WHERE id = ?",
        (id,)
    )

    os.remove(f"server/instance/articles/{id}")

    comment_id = db.execute(
        "SELECT id"
        " FROM comment"
        " WHERE post_id = ?",
        (id,)
    )
    for i in comment_id:
        db.execute(
            "DELETE FROM list"
            " WHERE remote_id = ?",
            (i["id"],)
        )

    db.execute(
        "DELETE FROM comment"
        " WHERE post_id = ?",
        (id,)
    )

    db.execute(
        "DELETE FROM list"
        " WHERE remote_id = ?",
        (id,)
    )

    db.commit()

    print(f"deleted {id}")

    return jsonify({"status": "success"})
