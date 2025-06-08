import falcon
import re
import json

# JSON serialization/deserialization is handled by Falcon using the `req.media` and `resp.media` attributes.
# This allows for easy handling of JSON data in requests and responses.
# In-memory database (temporary)
fake_database = []

class UserResource:
    def on_post(self, req, resp):
        """Handle POST - Create a new user"""
        try:
            data = req.media
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            # Validation
            if not username or not email or not password:
                resp.status = falcon.HTTP_400
                resp.media = {"error": "All fields (username, email, password) are required."}
                return

            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                resp.status = falcon.HTTP_400
                resp.media = {"error": "Invalid email format."}
                return

            if len(password) < 8:
                resp.status = falcon.HTTP_400
                resp.media = {"error": "Password must be at least 8 characters."}
                return

            # Save to fake database
            user = {
                "id": len(fake_database) + 1,
                "username": username,
                "email": email
            }
            fake_database.append(user)

            resp.status = falcon.HTTP_201
            resp.media = {
                "message": "User created successfully!",
                "user": user
            }

        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": "Server error", "details": str(e)}

    def on_get(self, req, resp):
        """Handle GET - Return list of users"""
        try:
            resp.status = falcon.HTTP_200
            resp.media = {
                "users": fake_database,
                "total_users": len(fake_database)
            }
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": "Server error", "details": str(e)}

# Create Falcon app
app = falcon.App()

# Add route
app.add_route('/users', UserResource())
app.add_route('/users/{user_id}', UserResource())
