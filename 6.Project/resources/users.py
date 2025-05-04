import json
import falcon
from db import get_db_connection
from auth import generate_token

class SignupResource:
    def on_post(self, req, resp):
        data = json.load(req.bounded_stream)
        username = data["username"]
        password = data["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            resp.media = {"message": "User created"}
        except:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Username already exists"}
        finally:
            conn.close()

class LoginResource:
    def on_post(self, req, resp):
        data = json.load(req.bounded_stream)
        username = data["username"]
        password = data["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            token = generate_token(username)
            resp.media = {"token": token}
        else:
            resp.status = falcon.HTTP_401
            resp.media = {"error": "Invalid credentials"}
