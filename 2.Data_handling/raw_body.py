"""
In Falcon, handling raw request bodies (such as JSON, XML, or any other
arbitrary body data) involves reading the raw body content directly from 
the request and parsing it yourself if necessary. This is useful when you're
dealing with custom data formats or APIs that send raw payloads (e.g., application/json, text/plain, etc.).
This example demonstrates how to handle raw request bodies in a Falcon application.
"""
import falcon

# Function to create a structured response
def create_response(status_code, data, message=None):
    response = {
        "status": "success" if status_code < 400 else "error",
        "data": data,
        "message": message if message else None
    }
    return str(response)

# Resource to handle raw body data (Plain Text)
class RawTextBodyResource:
    def on_post(self, req, resp):
        """Handles POST requests with raw text body."""
        
        # Get the raw body (req.bounded_stream is a stream, so we read it into a variable)
        raw_body = req.bounded_stream.read().decode('utf-8')  # Decode bytes to string
        
        # Process the raw text (for example, logging it or performing operations)
        print(f"Received Text: {raw_body}")
        
        # Return a success response
        resp.status = falcon.HTTP_200
        resp.body = create_response(falcon.HTTP_200, {
            "received_text": raw_body
        })

# Create the Falcon app
app = falcon.App()

# Add the route for raw text body data handling
raw_text_body_resource = RawTextBodyResource()
app.add_route('/rawtext', raw_text_body_resource)

# Running the Falcon app with WSGI server
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('127.0.0.1', 8000, app)
    print("Serving on http://127.0.0.1:8000/rawtext")
    httpd.serve_forever()
