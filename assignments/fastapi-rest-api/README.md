# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Build a simple REST API using FastAPI. You'll design endpoints, define request and response models, and practice implementing basic CRUD (Create, Read, Update, Delete) operations.

## 📝 Tasks

### 🛠️ Setup and Run Your API Server

#### Description
Set up a FastAPI application and run it locally using `uvicorn`.

#### Requirements
Completed program should:

- Use FastAPI to create an app instance.
- Include instructions in this README for how to install dependencies and run the server.
- Run without errors and serve the API on `http://localhost:8000`.

### 🛠️ Create CRUD Endpoints for an Item Resource

#### Description
Implement an in-memory item store and provide endpoints to create, read, update, and delete items.

#### Requirements
Completed program should:

- Define a `Pydantic` model called `Item` with the fields:
  - `id`: `int`
  - `name`: `str`
  - `description`: `str | None`
  - `price`: `float`
- Provide the following endpoints:
  - `GET /items`: return a list of all items.
  - `GET /items/{item_id}`: return a single item by `id` (return 404 if not found).
  - `POST /items`: create a new item and return it.
  - `PUT /items/{item_id}`: update an existing item by `id` (return 404 if not found).
  - `DELETE /items/{item_id}`: delete an item by `id` (return 404 if not found).
- Use proper HTTP status codes (e.g., 200, 201, 404).

### 🛠️ Add Query Parameters and Validation

#### Description
Extend your API with query parameters to filter results and validate request data.

#### Requirements
Completed program should:

- Support an optional query parameter `min_price` for `GET /items` that returns only items with `price` greater than or equal to the provided value.
- Validate input so that `price` cannot be negative.
- Return clear error messages when validation fails.

---

## 🧪 Bonus (Optional)

- Add an endpoint `GET /items/search` that accepts a `q` query parameter and returns matching items by name or description.
- Add OpenAPI documentation notes using FastAPI's `summary` and `description` parameters.

---

## 🚀 Getting Started

1. Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

2. Run the server:

```bash
uvicorn starter-code:app --reload
```

3. Open the interactive API docs:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
