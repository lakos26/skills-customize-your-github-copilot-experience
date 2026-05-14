# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to practice routing, request handling, and JSON responses. You will create endpoints for reading, creating, and managing simple data in memory.

## 📝 Tasks

### 🛠️ Create the API Application

#### Description

Set up a FastAPI application and add a basic root endpoint so the API can respond to requests.

#### Requirements

Completed program should:

- Create a FastAPI app instance.
- Add a `GET /` endpoint that returns a welcome message.
- Run without errors when started locally.

### 🛠️ Build Read and Create Endpoints

#### Description

Add endpoints that return a list of items and allow new items to be added through JSON requests.

#### Requirements

Completed program should:

- Add a `GET /items` endpoint that returns all stored items.
- Add a `POST /items` endpoint that accepts JSON input.
- Store new items in memory while the application is running.
- Return JSON responses for both endpoints.

### 🛠️ Add Validation and Status Codes

#### Description

Improve the API by checking incoming data and returning appropriate HTTP responses.

#### Requirements

Completed program should:

- Validate required fields in the request body.
- Return a `400` or `422` response when input is invalid.
- Return a `201` response when a new item is created.
- Keep the API structure clear and easy to extend.
