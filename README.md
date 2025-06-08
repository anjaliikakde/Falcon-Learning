# Falcon Learning Guide

# 📑 Table of Contents
- [About Falcon](#about-falcon)
- [Understanding API](#understanding-api)
- [REST API Concepts](#rest-api-concepts)
- [Running a Falcon Server](#running-a-falcon-server)
- [HTTP Methods in Falcon](#http-methods-in-falcon)
- [Falcon Routes](#testing-falcon-routes)
  - [Using Postman](#using-postman)
  - [Using Curl](#using-curl)
- [Handling Different Data Formats using Falcon ](#handling-different-data-formats)
- [CRUD Operations with SQLite in Falcon](#crud-operations-with-sqlite)
- [Testing APIs with Pytest](#testing-with-pytest)
- [Final Mini Project](#final-mini-project)


# [Falcon](#about-falcon)
Falcon is a high-performance, minimalist Python web framework designed for building fast, scalable REST APIs and microservices, giving developers full control over request handling, routing, and responses with minimal overhead.

# [Understanding API](#understanding-api)
API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. It defines the methods and data formats that applications use to request and exchange information.


```  
API = A way for two software programs to talk to each other and share information.

```
# [REST API Concepts](#rest-api-concepts)

REST API (Representational State Transfer API) is a way for two computer systems to talk to each other over the internet, using simple rules.
It uses normal HTTP methods like GET, POST, PUT, and DELETE to work with resources (like users, products, or anything you want).

Each thing (resource) is given a URL (like a web address), and you use different methods to create, read, update, or delete that thing.

It always tries to be simple, organized, and stateless — meaning each request should have all the information it needs, without depending on previous ones.

# [Running a Falcon Server](#running-a-falcon-server)

## 1. Install Falcon
Open Command Prompt and type:
```
pip install falcon

```
## 2. Install waitress (Better for Windows)
Install waitress:
```
pip install waitress

```
You can do it by creating virtual environment and then install the requirements.txt file and activate the venv.


## 3. Create a Simple Falcon App
Open VS Code.

Write this code and save it as app.py:
```
import falcon

class HelloResource:
    def on_get(self, req, resp):
        resp.media = {"message": "Hello, World from Falcon on Windows!"}

app = falcon.App()
app.add_route('/hello', HelloResource())
```
## 4. Run the Server with Waitress
In Command Prompt, go to your app folder and run:

```
waitress-serve --port=8000 app:app

```
✨ Now the server will start on:
```
http://127.0.0.1:8000/hello

```
You’ll see:
```
{"message": "Hello, World from Falcon on Windows!"}

```
# [HTTP Methods in Falcon](#http-methods-in-falcon)

An HTTP method (or HTTP verb) is an action that you want to perform on a resource (data) when making a request to a web server. When you interact with a web server or API, you specify an HTTP method to define the action you want to perform on the requested resource.

Common HTTP Methods used in falcon 

## GET:
The GET method is used to retrieve data from the server. It requests a representation of the resource without making any changes to it.

#### Example:
 You visit a website to view a blog post. The web server sends you the content of that blog post.

## POST:
 The POST method is used to send data to the server. It's typically used for creating a new resource or submitting data (e.g., filling out a form).

####  Example: 
When you sign up for a new account on a website, your data (name, email, etc.) is sent to the server.
## PUT:
 The PUT method is used to update an existing resource or create a resource at a specific URI (Uniform Resource Identifier). It replaces the entire resource.

#### Example: 
When you update your email address on your profile, the existing data is replaced with the new data.
## DELETE:
 The DELETE method is used to remove a specified resource from the server.

#### Example: 
When you delete an old post or remove your account, the server removes the data.

## PATCH:
  The PATCH method is used to partially update a resource on the server. Unlike PUT, which replaces the entire resource, PATCH only modifies the specified parts.

#### Example:
Changing only the email address of your profile while keeping other data intact.
## OPTIONS:
 The OPTIONS method is used to describe the available methods or actions that can be performed on a resource. It is often used to check the capabilities of a server or resource.

#### Example: 
Before interacting with an API, you might want to check which HTTP methods are allowed for a particular endpoint.

## HEAD:
 The HEAD method is similar to GET, but it only retrieves the headers of the resource, without the body. It's typically used to check metadata (like content type or length) of a resource.

#### Example: 
You might want to check the size of a file before downloading it.
## TRACE:
The TRACE method is used to perform a diagnostic test by returning the request message as a response. It helps debug or trace the path the request takes through the network.

#### Example: 
It's like a network troubleshooting tool to trace the request path.

 All these HTTP methods have standard method names that correspond to the respective HTTP method actions. **Each method in Falcon has a corresponding function that **you can implement in your resource class** to handle requests for that HTTP method.**

Standard method nmaes are given below :
 

| **HTTP Method** | **Falcon Method**             | **Purpose**                                           |
|-----------------|-------------------------------|-------------------------------------------------------|
| **GET**         | `on_get(self, req, resp)`      | Handle GET requests (retrieve data)                  |
| **POST**        | `on_post(self, req, resp)`     | Handle POST requests (send data/create resources)    |
| **PUT**         | `on_put(self, req, resp)`      | Handle PUT requests (update data/replace resource)   |
| **DELETE**      | `on_delete(self, req, resp)`   | Handle DELETE requests (remove resource)             |
| **PATCH**       | `on_patch(self, req, resp)`    | Handle PATCH requests (partially update resource)    |
| **OPTIONS**     | `on_options(self, req, resp)`  | Handle OPTIONS requests (describe allowed methods)   |
| **HEAD**        | `on_head(self, req, resp)`     | Handle HEAD requests (retrieve headers only)         |
| **TRACE**       | `on_trace(self, req, resp)`    | Handle TRACE requests (debugging tool)               |


# [Falcon Routes](#testing-falcon-routes)

In Falcon, a route refers to a specific URL pattern that is mapped to a resource (class or function) that handles requests for that URL. When a client (like a browser, Postman, or cURL) sends an HTTP request to a specific URL (or path), Falcon determines which route matches that URL and invokes the corresponding resource to handle the request.
You can see it in the code, this urls gives us diffrent responses based on change in urls, make sure to use correct url for your http requests.


**Postman** is a popular API testing tool that allows developers and testers to easily send HTTP requests, analyze responses, and automate API testing. It is widely used to test RESTful APIs (and other types of APIs), inspect their behavior, and debug the API responses during the development process. Learn about postman: <br>

[![Postman Docs](https://img.shields.io/badge/Postman-Learn%20More-orange?logo=postman)](https://learning.postman.com/docs/introduction/overview/) 

**cURL** (short for "Client URL") is a command-line tool and library used to transfer data over a network. It allows you to send and receive data between your computer and a server using various internet protocols like HTTP, HTTPS, FTP, and more.

 [![Test cURL Online](https://img.shields.io/badge/ReqBin-Test%20cURL%20Online-blue?logo=curl)](https://reqbin.com/curl) 
   &nbsp; [![Test cURL Online](https://img.shields.io/badge/Test%20cURL%20Online-ReqBin-brightgreen?logo=curl)](https://reqbin.com/curl)

#  [Handling Different Data Formats using Falcon](#handling-different-data-formats)

In Falcon we can handle diffrent data formats, which are given below :

- JSON
- Form data 
- Headers
- Query parameter
- Row body
- Files 


## JSON
Falcon automatically parses incoming JSON data if the Content-Type is set to application/json. You can access the parsed data using req.media.

## Form Data

URL-encoded Form Data (application/x-www-form-urlencoded):
Falcon can automatically parse URL-encoded form data if the auto_parse_form_urlencoded option is enabled. You can access the parsed parameters using req.params.

### Multipart Form Data (multipart/form-data):
Falcon supports handling multipart form data, which is commonly used for file uploads. You can access the files using req.files.

## Headers
You can access HTTP headers using methods like req.get_header(name) or req.headers. Falcon provides convenient attributes for common headers, such as req.content_type and req.accept.

## Query Parameters
Query parameters are accessible via req.params. Falcon automatically parses the query string and makes the parameters available.

## Raw Body
You can access the raw request body using req.stream.read(). This is useful when dealing with non-standard content types or when you need to handle the body manually.

## Files
Falcon supports handling file uploads through multipart form data. Files can be accessed via req.files, which provides a dictionary-like object containing the uploaded files.

Implementation of this section you will found in `2.Data_handling folder`.

#  [CRUD Operations with SQLite in Falcon](#crud-operations-with-sqlite)

CRUD stands for Create, Read, Update, Delete, which are the four basic operations you can perform on database records. In the context of Falcon + SQLite, this means building RESTful APIs that interact with an SQLite database to:

## CRUD Operations mapping

| **Operation** | **HTTP Method** | **Purpose**                                   |
|---------------|------------------|-----------------------------------------------|
| **Create**    | `POST`           | Add a new record to the database              |
| **Read**      | `GET`            | Retrieve existing records                     |
| **Update**    | `PUT` / `PATCH`  | Modify existing records                       |
| **Delete**    | `DELETE`         | Remove records from the database              |

These methods handle the logic for interacting with your SQLite database using standard SQL queries like `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.

Implementation of this part is in `3.CRUD` folder.

> Falcon is ideal for building high-performance microservices where you can keep the code clean, testable, and close to the metal.

# [Testing APIs with Pytest](#testing-with-pytest)

pytest is a no-boilerplate testing framework that supports simple assert statements for writing tests, automatic test discovery, fixtures for setup/teardown, and rich plugin support for scaling complex test suites. 

[![Pytest Documentation 📘](https://img.shields.io/badge/Pytest-Documentation-blue)](https://docs.pytest.org/en/stable/)

In simpler terms, pytest is a tool used to test if your Python code works correctly.
It helps you write test functions that check whether your code gives the expected output.

**In Falcon**, pytest is commonly used for testing the API endpoints and verifying that the routes, request handling, and responses work as expected. Since Falcon is a lightweight web framework, using pytest helps ensure that your Falcon app functions correctly and handles HTTP requests and responses properly.

# [Final Mini Project](#final-mini-project)
This final mini project is a Blog Post App developed using Streamlit for the frontend. To run the application, use the following command in your terminal:

```
streamlit run streamlit_app.py
```
Make sure you are in right directory.
 
The Blog Post App is a simple yet effective web application designed using Streamlit, which allows users to create, view, and manage blog posts in a clean and interactive interface. This app serves as a platform where users can write blog entries using a text input area, and instantly see their posts displayed on the same page. 
# [Streamlit app url](https://falcon-learning-si7yvfwjiyawjk5pjwtrat.streamlit.app/)
