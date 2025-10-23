# 🚀 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. You will create endpoints, handle requests and responses, and understand basic API concepts.

## 📝 Tasks

### 🛠️ Create a Simple FastAPI Application

#### Description
Set up a FastAPI project and create a basic API with at least two endpoints.

#### Requirements
Completed program should:
- Use FastAPI to create a web server
- Implement a root endpoint (`/`) that returns a welcome message
- Implement a `/items/{item_id}` endpoint that returns details for a given item

### 🛠️ Add Data and Error Handling

#### Description
Enhance your API to handle data and errors gracefully.

#### Requirements
Completed program should:
- Use a Python dictionary or list to store item data
- Return a 404 error if an item is not found
- Validate input types and handle invalid requests

### 🛠️ (Optional) Add a POST Endpoint

#### Description
Allow users to add new items to your API using a POST request.

#### Requirements
Completed program should:
- Accept JSON data in the request body
- Add the new item to your data store
- Return a success message and the added item
