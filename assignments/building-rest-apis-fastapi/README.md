# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API using the FastAPI framework. Students will create routes, work with JSON data, and practice request validation and response handling in a modern Python web API.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Set up a basic FastAPI app that serves a simple API for managing books or tasks.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app.
- Define a root endpoint that returns a welcome message.
- Run the app locally with a development server.
- Use a simple in-memory data store to hold records.

### 🛠️ Build CRUD Endpoints

#### Description
Create API routes to create, read, update, and delete items.

#### Requirements
Completed program should:

- Add a `GET /items` route that returns all stored items.
- Add a `GET /items/{item_id}` route that returns one item by ID.
- Add a `POST /items` route that accepts JSON data and creates a new item.
- Add a `PUT /items/{item_id}` route that updates an existing item.
- Add a `DELETE /items/{item_id}` route that removes an item.
- Return JSON responses that follow a clear structure.

### 🛠️ Validate Input and Handle Errors

#### Description
Improve the API by validating request data and handling common errors gracefully.

#### Requirements
Completed program should:

- Use Pydantic models to validate request bodies.
- Reject invalid input with clear validation errors.
- Return a `404` response when an item is not found.
- Ensure the API responds with proper JSON for success and error cases.

### 🛠️ Example Data Model

#### Description
Use a simple item model for your API.

#### Requirements
Completed program should:

- Define a model with fields such as `id`, `title`, and `description`.
- Accept input in JSON format like:

```json
{
  "title": "FastAPI Guide",
  "description": "Learn how to build APIs with FastAPI"
}
```

- Return output similar to:

```json
{
  "id": 1,
  "title": "FastAPI Guide",
  "description": "Learn how to build APIs with FastAPI"
}
```

