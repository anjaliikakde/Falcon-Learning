import json
import falcon
from db import get_db_connection
from auth import authenticate

class CommentResource:
    def on_post(self, req, resp, post_id):
        token = req.get_header("Authorization")
        if not token:
            raise falcon.HTTPUnauthorized("Missing token")

        username = authenticate(token)
        data = json.load(req.bounded_stream)
        content = data["content"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO comments (post_id, content, author) VALUES (?, ?, ?)", (post_id, content, username))
        conn.commit()
        conn.close()

        resp.media = {"message": "Comment added"}

    def on_get(self, req, resp, post_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, content, author FROM comments WHERE post_id = ?", (post_id,))
        comments = cursor.fetchall()
        conn.close()

        result = []
        for cid, content, author in comments:
            result.append({
                "id": cid,
                "author": author,
                "content": content
            })
        resp.media = result
