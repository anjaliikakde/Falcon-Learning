import jwt
import falcon
import datetime

SECRET = "super-secret-development-key-123456789"

def generate_token(username):
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def authenticate(token):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload["username"]
    except jwt.ExpiredSignatureError:
        raise falcon.HTTPUnauthorized("Token expired")
    except:
        raise falcon.HTTPUnauthorized("Invalid token")
