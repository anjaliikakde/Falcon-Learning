# Falcon Learning Guide

# 📑 Table of Contents
- [About Falcon](#about-falcon)
- [Understanding API](#understanding-api)
- [REST API Concepts](#rest-api-concepts)
- [Running a Falcon Server](#running-a-falcon-server)
- [HTTP Methods in Falcon](#http-methods-in-falcon)
- [Testing Falcon Routes](#testing-falcon-routes)
  - [Using Postman](#using-postman)
  - [Using Curl](#using-curl)
- [Handling Routes in Falcon](#handling-routes-in-falcon)
- [Handling Different Data Formats](#handling-different-data-formats)
- [CRUD Operations with SQLite](#crud-operations-with-sqlite)
- [Testing with Pytest](#testing-with-pytest)
- [Final Mini Project](#final-mini-project)


# [Falcon](#about-falcon)
Falcon is a high-performance, minimalist Python web framework designed for building fast, scalable REST APIs and microservices, giving developers full control over request handling, routing, and responses with minimal overhead.

# [API](#understanding-api)
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
✅ Now the server will start on:
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
