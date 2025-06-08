import falcon
import json

# Simple function to create a structured response
def create_response(status_code, data, message=None):
    response = {
        "status": "success" if status_code < 400 else "error",
        "data": data,
        "message": message if message else None
    }
    return json.dumps(response)

# Resource for handling query parameters
class QueryParameterResource:
    def on_get(self, req, resp):
        """Handles GET requests with query parameters."""
        
        # Extract query parameters from the request
        name = req.get_param('name', default=None)  # Default is None if 'name' is not provided
        age = req.get_param('age', default=None)
        
        if not name or not age:
            resp.status = falcon.HTTP_400
            resp.body = create_response(falcon.HTTP_400, {}, "Both 'name' and 'age' query parameters are required.")
            return

        # Process the query parameters
        try:
            age = int(age)  # Ensure age is an integer
            if age <= 0:
                raise ValueError("Age must be a positive number.")

            # Return a success response
            resp.status = falcon.HTTP_200
            resp.body = create_response(falcon.HTTP_200, {
                "name": name,
                "age": age
            })
        
        except ValueError as e:
            resp.status = falcon.HTTP_400
            resp.body = create_response(falcon.HTTP_400, {}, str(e))

# Create the Falcon app
app = falcon.App()

# Add a route that expects query parameters
query_resource = QueryParameterResource()
app.add_route('/user', query_resource)

# Running the Falcon app with WSGI server
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('0.0.0.0', 8000, app)
    print("Serving on http://127.0.0.1:8000/user?name=John&age=30")
    httpd.serve_forever()


"""This file can run using python filname.py commond."""