<div align="center">

# ⚡ FastAPI E-Commerce Backend
### Category & Product Management REST API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://mysql.com)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://sqlalchemy.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> A production-ready RESTful backend built with **FastAPI**, featuring modular architecture, relational database design, server-side pagination, and auto-generated Swagger UI documentation.

[🚀 API Docs](#-api-endpoints) • [⚙️ Setup](#%EF%B8%8F-installation) • [📐 Architecture](#-project-architecture) • [🗄️ Database](#%EF%B8%8F-database-design)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔁 **Full CRUD** | Create, Read, Update, Delete for Categories & Products |
| 🔗 **Relational Design** | One-to-Many: Category → Products via SQLAlchemy ORM |
| 📄 **Pagination** | Server-side pagination on all list endpoints |
| ✅ **Data Validation** | Request validation & response serialisation with Pydantic |
| 📖 **Auto Docs** | Swagger UI + ReDoc auto-generated via OpenAPI |
| 🏗️ **Modular Architecture** | Clean separation: API layer → Service layer → DB layer |
| 🧪 **API Testing** | Tested with Postman & Swagger UI |

---

## 🛠️ Tech Stack

```
Backend       →  Python 3.10+  |  FastAPI  |  Uvicorn
ORM           →  SQLAlchemy 2.0  |  Pydantic v2
Database      →  MySQL 8.0
API Testing   →  Postman  |  Swagger UI (built-in)
Dev Tools     →  Git  |  VS Code  |  Virtual Environment
```

---

## 📐 Project Architecture

```
fastapi-machine-test/
│
├── app/
│   ├── main.py              # App entry point, router registration
│   ├── database.py          # DB engine, session, base config
│   │
│   ├── models/
│   │   ├── category.py      # Category SQLAlchemy model
│   │   └── product.py       # Product SQLAlchemy model
│   │
│   ├── schemas/
│   │   ├── category.py      # Pydantic request/response schemas
│   │   └── product.py       # Pydantic request/response schemas
│   │
│   ├── routers/
│   │   ├── category.py      # Category API route handlers
│   │   └── product.py       # Product API route handlers
│   │
│   └── services/
│       ├── category.py      # Category business logic
│       └── product.py       # Product business logic
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🗄️ Database Design

```
┌─────────────────────┐          ┌──────────────────────────┐
│      Category        │          │         Product           │
├─────────────────────┤          ├──────────────────────────┤
│ id       INT (PK)   │◄────┐    │ id          INT (PK)     │
│ name     VARCHAR    │     └────│ category_id INT (FK)     │
└─────────────────────┘          │ name        VARCHAR      │
                                  │ price       DECIMAL      │
                                  └──────────────────────────┘
         One Category  ───────────────────►  Many Products
```

**Relationship:** `One-to-Many` — A single category can have multiple products. Foreign key enforced at DB level via SQLAlchemy ORM.

---

## 🚀 API Endpoints

### 📁 Category APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/categories?page=1` | Get all categories (paginated) |
| `POST` | `/api/categories` | Create a new category |
| `GET` | `/api/categories/{id}` | Get category by ID |
| `PUT` | `/api/categories/{id}` | Update category by ID |
| `DELETE` | `/api/categories/{id}` | Delete category by ID |

### 📦 Product APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/products?page=1` | Get all products with category (paginated) |
| `POST` | `/api/products` | Create a new product |
| `GET` | `/api/products/{id}` | Get product with category details |
| `PUT` | `/api/products/{id}` | Update product by ID |
| `DELETE` | `/api/products/{id}` | Delete product by ID |

> 📖 **Interactive Docs:** Once server is running, visit:
> - Swagger UI → `http://127.0.0.1:8000/docs`
> - ReDoc → `http://127.0.0.1:8000/redoc`

---

## ⚙️ Installation

### Prerequisites
- Python 3.10+
- MySQL 8.0+
- Git

### Step-by-Step Setup

**1. Clone the repository**
```bash
git clone https://github.com/sakshimalkar/fastapi-machine-test.git
cd fastapi-machine-test
```

**2. Create & activate virtual environment**
```bash
# Create
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure database**

Create a MySQL database:
```sql
CREATE DATABASE fastapi_db;
```

Update `app/database.py` with your credentials:
```python
DATABASE_URL = "mysql+pymysql://root:yourpassword@localhost/fastapi_db"
```

**5. Run the server**
```bash
uvicorn app.main:app --reload
```

Server starts at → **http://127.0.0.1:8000**
Swagger UI → **http://127.0.0.1:8000/docs**

---

## 🧪 Sample API Usage

**Create a Category**
```bash
curl -X POST "http://127.0.0.1:8000/api/categories" \
  -H "Content-Type: application/json" \
  -d '{"name": "Electronics"}'
```

**Response**
```json
{
  "id": 1,
  "name": "Electronics"
}
```

**Create a Product**
```bash
curl -X POST "http://127.0.0.1:8000/api/products" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "price": 75000, "category_id": 1}'
```

**Response**
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 75000,
  "category": {
    "id": 1,
    "name": "Electronics"
  }
}
```

**Get Products with Pagination**
```bash
curl "http://127.0.0.1:8000/api/products?page=1"
```

---

## 📦 Dependencies

```txt
fastapi
uvicorn
sqlalchemy
pymysql
pydantic
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 👩‍💻 Author

<div align="center">

**Sakshi Malkar**
Full Stack Developer | Python · FastAPI · React.js

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/sakshi-malkar)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/sakshimalkar)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-00f0d0?style=for-the-badge&logo=googlechrome&logoColor=white)](https://sakshimalkar.github.io/portfolio)

</div>

---

<div align="center">
  <sub>Built with ❤️ using FastAPI · SQLAlchemy · MySQL · Pydantic</sub>
</div>
