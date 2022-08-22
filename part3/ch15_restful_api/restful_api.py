import json
import datetime
from dataclasses import dataclass
from flask import request, Flask, Blueprint

bp = Blueprint("v1", __name__, url_prefix="/v1")

posts = {}
post_number = 1


@dataclass
class BlogPost:
    title: str
    contents: str
    date: str


@bp.route("/posts", methods=["POST"])
def write_post():
    request_json = request.get_json()
    title = request_json["title"]
    contents = request_json["contents"]

    if len(title) == 0 or len(contents) == 0:
        return "Bad request", 400

    global post_number

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"title = {title}, contents = {contents}, date = {now}. post_number = {post_number}")

    posts[post_number] = BlogPost(title=title, contents=contents, date=now)
    post_number += 1

    return "OK", 200


@bp.route("/posts/<int:number>", methods=["GET"])
def get_post(number):
    post = posts[number]
    if not post:
        return "Bad request", 400

    posts_json = [{"title": post.title,
                   "contents": post.contents,
                   "date": post.date,
                   "number": number}]
    response_json = {"post": posts_json}

    try:
        return json.dumps(response_json, ensure_ascii=False)
    except json.JSONDecodeError:
        return "Internal Server Error", 500


@bp.route("/posts", methods=["GET"])
def get_posts():
    posts_size = request.args.get("size", "-1")
    posts_size = int(posts_size)

    posts_json = []
    posts_acquired = 0

    for number in posts:
        post = posts[number]
        posts_json.append({"title": post.title,
                           "contents": post.contents,
                           "date": post.date,
                           "number": number})

        posts_acquired += 1
        if 0 <= posts_size <= posts_acquired:
            break

    response_json = {"posts": posts_json}
    try:
        return json.dumps(response_json, ensure_ascii=False)
    except json.JSONDecodeError:
        return "Internal Server Error", 500


@bp.route("/posts/<int:number>", methods=["PUT"])
def update_post(number):
    post = posts[number]
    if not post:
        return "Bad request", 400

    request_json = request.get_json()
    title = request_json["title"]
    contents = request_json["contents"]

    if len(title) == 0 or len(contents) == 0:
        return "Bad request", 400

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"title = {title}, contents = {contents}, date = {now}. post_number = {number}")

    posts[number] = BlogPost(title=title, contents=contents, date=now)

    return "OK", 200


@bp.route("/posts/<int:number>", methods=["DELETE"])
def delete_post(number):
    post = posts[number]
    if not post:
        return "Bad request", 400

    del posts[number]
    return "OK", 200


app = Flask(__name__)
app.register_blueprint(bp)
app.url_map.strict_slashes = False
app.run()
