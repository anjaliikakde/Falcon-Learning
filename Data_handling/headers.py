import falcon
import json

# Function to create a structured response
def create_response(status_code, data, message=None):
    response = {
        "status": "success" if status_code < 400 else "error",
        "data": data,
        "message": message if message else None
    }
    return json.dumps(response)

# Resource for handling headers
class HeaderResource:
    def on_get(self, req, resp):
        """Handles GET requests and extracts headers from the request."""

        # Accessing request headers
        user_agent = req.get_header('User-Agent', default='Unknown')
        content_type = req.get_header('Content-Type', default='Unknown')

        # Log the headers (for demonstration purposes)
        print(f"User-Agent: {user_agent}")
        print(f"Content-Type: {content_type}")

        # Process the headers
        response_data = {
            "User-Agent": user_agent,
            "Content-Type": content_type
        }

        # Set custom response headers
        resp.set_header('X-Custom-Header', 'CustomHeaderValue')
        resp.set_header('X-Request-Processed', 'True')

        # Return response with headers data
        resp.status = falcon.HTTP_200
        resp.body = create_response(falcon.HTTP_200, response_data)

# Create Falcon app
app = falcon.App()

# Add a route that expects to handle headers
header_resource = HeaderResource()
app.add_route('/headers', header_resource)

# Running the Falcon app with WSGI server
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('127.0.0.1', 8000, app)
    print("Serving on http://127.0.0.1:8000/headers")
    httpd.serve_forever()

# This code creates a simple Falcon web application that handles GET requests to the /headers endpoint.