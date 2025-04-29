"""
To handle form data in Falcon, you can easily use the req.get_param()
method to extract individual form fields. Form data is typically sent 
via POST requests with the content type application/x-www-form-urlencoded
(standard HTML form submission) or multipart/form-data (for file uploads).
This example demonstrates how to handle form data in a Falcon application.
"""
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

# Resource to handle form data
class FormDataResource:
    def on_post(self, req, resp):
        """Handles POST requests and extracts form data."""
        
        # Accessing form data (using req.get_param() for individual parameters)
        name = req.get_param('name', required=True)  # 'name' is required
        email = req.get_param('email', required=True)  # 'email' is required
        age = req.get_param('age', default=None)

        # Process the form data
        if not name or not email:
            resp.status = falcon.HTTP_400
            resp.body = create_response(falcon.HTTP_400, {}, "Both 'name' and 'email' are required.")
            return

        # Return a success response with the form data
        resp.status = falcon.HTTP_200
        resp.body = create_response(falcon.HTTP_200, {
            "name": name,
            "email": email,
            "age": age if age else "Not Provided"
        })

# Create the Falcon app
app = falcon.App()

# Add the route for form data handling
form_data_resource = FormDataResource()
app.add_route('/submit', form_data_resource)

# Running the Falcon app with WSGI server
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('127.0.0.1', 8000, app)
    print("Serving on http://127.0.0.1:8000/submit")
    httpd.serve_forever()
