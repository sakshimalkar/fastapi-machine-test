# FastAPI Machine Test

## Tech Stack

* FastAPI
* Python
* SQLAlchemy ORM
* MySQL
* RESTful API

---

# Installation Steps

### 1. Clone Repository

git clone <repo-link>

### 2. Navigate to project

cd fastapi-machine-test

### 3. Create Virtual Environment

python -m venv venv

### 4. Activate Virtual Environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 5. Install Dependencies

pip install -r requirements.txt

---

# Database Setup

Create MySQL database:

CREATE DATABASE fastapi_db;

Update database credentials in:

app/database.py

Example:

mysql+pymysql://root:password@localhost/fastapi_db

---

# Run Server

uvicorn app.main:app --reload

Server will start at:

http://127.0.0.1:8000

Swagger API docs:

http://127.0.0.1:8000/docs

---

# API Endpoints

## Category APIs

GET /api/categories?page=1
POST /api/categories
GET /api/categories/{id}
PUT /api/categories/{id}
DELETE /api/categories/{id}

## Product APIs

GET /api/products?page=1
POST /api/products
GET /api/products/{id}
PUT /api/products/{id}
DELETE /api/products/{id}

---

# Database Design

Category Table

| Column | Type    |
| ------ | ------- |
| id     | integer |
| name   | string  |

Product Table

| Column      | Type        |
| ----------- | ----------- |
| id          | integer     |
| name        | string      |
| price       | integer     |
| category_id | foreign key |

Relationship:

One Category → Many Products
