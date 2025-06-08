import falcon
from wsgiref import simple_server

from db import init_db
from resources.users import SignupResource, LoginResource
from resources.posts import PostResource
from resources.comments import CommentResource

# Initialize DB
init_db()

# Falcon App
app = falcon.App()

# Routes
app.add_route("/signup", SignupResource())
app.add_route("/login", LoginResource())
app.add_route("/posts", PostResource())
app.add_route("/posts/{post_id}/comments", CommentResource())

# Run server
if __name__ == "__main__":
    with simple_server.make_server("127.0.0.1", 8000, app) as httpd:
        print("Serving on http://127.0.0.1:8000")
        httpd.serve_forever()
