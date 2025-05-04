import json
import markdown
import falcon
from db import get_db_connection
from auth import authenticate

class PostResource:
    def on_post(self, req, resp):
        token = req.get_header("Authorization")
        if not token:
            raise falcon.HTTPUnauthorized("Missing token")

        username = authenticate(token)
        data = json.load(req.bounded_stream)
        title = data["title"]
        content = data["content"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)", (title, content, username))
        conn.commit()
        conn.close()

        resp.media = {"message": "Post created"}

    def on_get(self, req, resp):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, content, author FROM posts")
        posts = cursor.fetchall()
        conn.close()

        result = []
        for pid, title, content, author in posts:
            result.append({
                "id": pid,
                "title": title,
                "author": author,
                "content_html": markdown.markdown(content)
            })
        resp.media = result
