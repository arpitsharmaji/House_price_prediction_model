# 🏠 House Price Prediction API

A production-oriented Machine Learning API built using FastAPI, PostgreSQL, SQLAlchemy, Alembic, JWT Authentication, Docker, and AWS EC2.

The application enables authenticated users to generate, store, manage, and retrieve house price predictions while demonstrating modern backend engineering practices such as containerization, database migrations, secure authentication, environment-based configuration, and cloud deployment.

## 🚀 Features

### 🔐 Authentication & Authorization

* User Registration
* User Login
* JWT Token-Based Authentication
* Protected Routes
* Password Hashing
* User Authorization
* Secure Credential Validation
* Stateless Authentication

### 🏠 House Price Prediction

* Machine Learning-Based House Price Prediction
* Real-Time Prediction API
* Scikit-Learn Model Deployment
* Input Validation using Pydantic
* Prediction History Storage
* User-Specific Predictions

### 🗄 Database Management

* PostgreSQL Database
* SQLAlchemy ORM
* Database Relationships
* Alembic Migrations
* Environment-Based Configuration
* Persistent Database Storage

### 🐳 Containerization & Deployment

* Dockerized Application
* Docker Compose Orchestration
* Containerized PostgreSQL
* Environment Variable Management
* AWS EC2 Deployment
* Persistent Volumes

---

# 🏗 Architecture

```text
                    AWS EC2
                        │
                Docker Compose
                        │
        ┌───────────────┴───────────────┐
        │                               │
 ┌───────────────┐              ┌───────────────┐
 │ FastAPI API   │─────────────▶│ PostgreSQL    │
 │ Container     │              │ Container     │
 └───────────────┘              └───────────────┘
                                        │
                                        ▼
                              Persistent Volume
```

---

# 🛠 Tech Stack

## Backend

* Python
* FastAPI
* Pydantic

## Database

* PostgreSQL
* SQLAlchemy
* Alembic

## Authentication & Security

* JWT
* Password Hashing
* Secure Authentication

## Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

## DevOps & Deployment

* Docker
* Docker Compose
* AWS EC2
* Git
* GitHub

---

# ⚙️ Environment Variables

Create a `.env` file in the project root.

```env
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=

DB_CONNECTION=

SECRET_KEY=
ALGORITHM=HS256
EXP_TIME=30
```

---

# 📂 Project Structure

```text
House_price_prediction_model/
│
├── app/
├── models/
├── alembic/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

---

# 🚀 Running with Docker

## Clone Repository

```bash
git clone git@github.com:arpitsharmaji/House_price_prediction_model.git

cd House_price_prediction_model
```

## Configure Environment

```bash
cp .env.example .env
```

Update the values in `.env`.

## Start Services

```bash
docker compose up -d
```

## Verify Containers

```bash
docker ps
```

## Apply Database Migrations

```bash
docker compose exec api alembic upgrade head
```

---

# 🌐 Access Application

FastAPI:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# 🔐 Authentication Endpoints

## Register User

```http
POST /user/register
```

## Login User

```http
POST /user/login_user
```

## Verify Authentication

```http
GET /user/is_auth
```

---

# 🏠 Prediction Endpoints

## Create Prediction

```http
POST /tasks/create
```

## Get All Predictions

```http
GET /tasks/all_tasks
```

## Get Prediction By ID

```http
GET /tasks/one_task/{task_id}
```

## Update Prediction

```http
PUT /tasks/update_task/{task_id}
```

## Delete Prediction

```http
DELETE /tasks/delete_task/{task_id}
```

---

# 🤖 Machine Learning Workflow

1. User submits house details.
2. Request is validated using Pydantic.
3. Features are preprocessed.
4. Trained Scikit-Learn pipeline is loaded.
5. Prediction is generated.
6. Prediction is stored in PostgreSQL.
7. Response is returned to the user.

---

# 🗄 Database Migrations

Apply migrations:

```bash
alembic upgrade head
```

Create migration:

```bash
alembic revision --autogenerate -m "migration_name"
```

Rollback migration:

```bash
alembic downgrade -1
```

---

# 📚 Key Concepts Demonstrated

* FastAPI Development
* REST API Design
* SQLAlchemy ORM
* Alembic Migrations
* PostgreSQL
* JWT Authentication
* Password Hashing
* Dependency Injection
* Machine Learning Model Deployment
* Docker
* Docker Compose
* Container Networking
* Persistent Volumes
* Environment Management
* AWS EC2 Deployment

---

# 🔮 Future Improvements

* GitHub Actions CI/CD
* Nginx Reverse Proxy
* HTTPS & SSL
* Redis Caching
* Role-Based Access Control (RBAC)
* MLflow Integration
* AWS RDS Migration
* Monitoring & Logging
* Kubernetes Deployment

---

# 👨‍💻 Author

**Arpit Sharma**

Backend Developer | FastAPI Developer | Machine Learning Enthusiast | MLOps Learner

GitHub: https://github.com/arpitsharmaji

---

# ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

