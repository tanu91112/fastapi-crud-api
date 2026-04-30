# Python FastAPI Backend – Book Management System (CRUD API)

A RESTful backend system built using FastAPI for managing books with full CRUD functionality. This project demonstrates backend development skills including API design, database integration, and request validation.

## Overview

## Overview

This API allows users to perform Create, Read, Update, and Delete (CRUD) operations on books stored in a database. It is built using FastAPI and tested using Swagger UI.

Built as a production-style backend service demonstrating API design, modular architecture, and scalable Python backend development.

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/martcpp/crud-api-fastapi.git
cd crud-api-fastapi
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
uvicorn app:app --reload
```

API will be available at:
```
http://localhost:8000
```

## Docker Setup

### 1. Build and run container
```bash
docker build -t crud-api .
docker run -p 8000:8000 crud-api
```

## API Documentation

Swagger UI:
```
http://localhost:8000/docs
```

## Endpoints

### GET /books/
Fetch all books

### POST /books/
Create a new book

Example request:
```json
{
  "title": "Example Book",
  "author": "John Doe",
  "year": 2024,
  "isbn": "978-3-16-148410-0"
}
```

### GET /books/{book_id}
Fetch a book by ID

### PUT /books/{book_id}
Update a book by ID

### DELETE /books/{book_id}
Delete a book by ID

## Data Schema

- id (integer): Unique identifier  
- title (string): Book title  
- author (string): Author name  
- year (integer): Publication year  
- isbn (string): ISBN number  

## Tech Stack

- Python (Core Language)
- FastAPI (Backend Framework)
- REST APIs (CRUD Operations)
- SQLAlchemy (ORM for Database Interaction)
- Uvicorn (ASGI Server)
- MySQL / PostgreSQL (Database Support)
- Pydantic (Data Validation)

## Note

Make sure Python is installed before running this project:
https://realpython.com/installing-python/