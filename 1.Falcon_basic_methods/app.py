"""
Falcon Basic HTTP Methods Example
This example demonstrates how to handle various HTTP methods in a Falcon web application.
It includes GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD, and TRACE methods.

"""
import falcon

class BasicResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.media = {"message": "GET request received. Fetching data..."}

    def on_post(self, req, resp):
        """Handles POST requests"""
        data = req.media  # media gets JSON body only
        resp.media = {"message": f"POST request received. Data created: {data}"}

    def on_put(self, req, resp):
        """Handles PUT requests"""
        data = req.media
        resp.media = {"message": f"PUT request received. Data updated: {data}"}

    def on_delete(self, req, resp):
        """Handles DELETE requests"""
        resp.media = {"message": "DELETE request received. Resource deleted."}

    def on_patch(self, req, resp):
        """Handles PATCH requests"""
        data = req.media
        resp.media = {"message": f"PATCH request received. Partially updated with: {data}"}

    def on_options(self, req, resp):
        """Handles OPTIONS requests"""
        resp.headers['Allow'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD, TRACE'
        resp.media = {"message": "OPTIONS request received. These methods are allowed."}

    def on_head(self, req, resp):
        """Handles HEAD requests"""
        resp.status = falcon.HTTP_200
        resp.content_length = 0  # No body content in HEAD

    def on_trace(self, req, resp):
        """Handles TRACE requests"""
        resp.media = {"message": "TRACE request received. Echoing request for debugging."}

# Create Falcon app instance
app = falcon.App()

# Add route
app.add_route('/basic', BasicResource())

"""
For testing the app, run the following command in the terminal:
waitress-serve --port 8000 app:app
and check it on url http://localhost:8000/basic or you can use tools like Postman or curl to
test the different HTTP methods.
Make sure to send the appropriate headers and body where required.
Also run the code in same directory as this file.

"""