"""
File Upload API using Falcon
In Falcon, handling file uploads typically involves reading the file data from the request,
processing it, and saving it if needed. Falcon provides an easy way to handle file uploads 
through the req.get_param() method, where you can access file parts sent in multipart/form-data 
format.
    
"""
import falcon
import os
import json

# Define a directory to save uploaded files
UPLOAD_DIRECTORY = 'uploads'

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

# Function to create a structured response
def create_response(status_code, data, message=None):
    response = {
        "status": "success" if status_code < 400 else "error",
        "data": data,
        "message": message if message else None
    }
    return json.dumps(response)

# Resource to handle file upload
class FileUploadResource:
    def on_post(self, req, resp):
        """Handles file upload requests."""
        
        # Get the uploaded file (assumed to be named 'file')
        uploaded_file = req.get_param('file')

        if uploaded_file is None:
            resp.status = falcon.HTTP_400
            resp.body = create_response(falcon.HTTP_400, {}, "No file uploaded.")
            return

        # Generate a safe filename (could use more sophisticated naming logic)
        file_path = os.path.join(UPLOAD_DIRECTORY, uploaded_file.filename)

        # Save the file to disk
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.file.read())
        
        # Respond with the location where the file was saved
        resp.status = falcon.HTTP_200
        resp.body = create_response(falcon.HTTP_200, {
            "filename": uploaded_file.filename,
            "file_path": file_path
        })

# Create the Falcon app
app = falcon.App()

# Add the route for file upload
file_upload_resource = FileUploadResource()
app.add_route('/upload', file_upload_resource)

# Running the Falcon app with WSGI server
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('127.0.0.1', 8000, app)
    print("Serving on http://127.0.0.1:8000/upload")
    httpd.serve_forever()
