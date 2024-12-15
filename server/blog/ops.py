from flask import Flask, jsonify, Blueprint, request
from markdown_it import MarkdownIt

from .db import get_db

post = Blueprint("post", __name__)
md = MarkdownIt("commonmark").enable("table")


@post.route("add", methods=["POST"])
def add_post():
    post_data = request.get_json()

    title = post_data.get("title")
    author = post_data.get("author")
    body = post_data.get("body")

    db = get_db()

    return jsonify({"status": "nihao"})  # TODO later


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
        if i["type"] == "post":
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
                # "sorting": int(entry["created"].timestamp())
            })
        elif i["type"] == "comment":
            entry = db.execute(
                "SELECT id, post_title, author, content, created"
                " FROM comment"
                " WHERE id = ?",
                (i["remote_id"],)
            ).fetchone()
            response_object["data"].append({
                "type": "comment",
                "id": entry["id"],
                "post_title": entry["post_title"],
                "author": entry["author"],
                "content": entry["content"],
                "created": entry["created"].strftime('%Y-%m-%d %H:%M:%S'),
                # "sorting": int(entry["created"].timestamp())
            })

    return jsonify(response_object)

    #
    # dbposts = db.execute(
    #     "SELECT p.id, title, description, created, author"
    #     " FROM post p"
    # ).fetchall()  # optimize needed
    #
    # response_object['data'] = []
    # for p in dbposts:
    #     post_data = {
    #         "type": "article",
    #         "id": p["id"],
    #         "title": p["title"],
    #         "desc": p["description"],
    #         "created": p["created"].strftime('%Y-%m-%d %H:%M:%S'),
    #         "author": p["author"],
    #         "sorting": int(p["created"].timestamp())
    #     }
    #     response_object["data"].append(post_data)
    #
    # dbcomments = db.execute(
    #     "SELECT c.id, post_title, author, content, created"
    #     " FROM comment c"
    # ).fetchall()
    #
    # for c in dbcomments:
    #     comment_data = {
    #         "type": "comment",
    #         "id": c["id"],
    #         "post_title": c["post_title"],
    #         "author": c["author"],
    #         "content": c["content"],
    #         "created": c["created"].strftime('%Y-%m-%d %H:%M:%S'),
    #         "sorting": int(c["created"].timestamp())
    #     }
    #     response_object["data"].append(comment_data)
    #
    # response_object["data"].sort(key=lambda x: x["sorting"], reverse=True)
    #
    # return jsonify(response_object)


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
        "SELECT p.id, title, author, body, created"
        " FROM post p"
        " WHERE p.id = ?",  # Adding WHERE clause to fetch the specific post by id
        (id,)
    ).fetchone()

    if post is None:
        return jsonify({"error": "Post not found"}), 404  # Return 404 if post doesn't exist

    # Format the post data similar to get_post_list
    post_data = {
        "id": post["id"],
        "title": post["title"],
        "author": post["author"],
        "body": md.render(post["body"]),
        "created": post["created"].strftime('%Y-%m-%d %H:%M:%S')
    }
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
        " ORDER BY created DESC",  # Query comments based on the post_id
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
    # comment = {
    #     "post_title": comment_data.get("post_title"),
    #     "author": comment_data.get("author"),
    #     "mail": comment_data.get("mail"),
    #     "content": comment_data.get("body"),
    # }
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
