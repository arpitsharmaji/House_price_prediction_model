# 🏠 House Price Prediction API

A secure, production-style FastAPI application that combines Machine Learning-based house price prediction with user authentication, authorization, database management, and RESTful APIs.

The project demonstrates practical backend engineering concepts including JWT Authentication, Password Hashing, SQLAlchemy ORM, Alembic migrations, Machine Learning model deployment, and protected API routes.

---

## 🚀 Features

### 🔐 Authentication & Authorization

- User Registration
- User Login
- JWT Token-Based Authentication
- Protected Routes
- User Authorization
- Password Hashing using bcrypt
- Secure Credential Validation
- Stateless Authentication

### 🏠 House Price Prediction

- Machine Learning House Price Prediction
- Real-Time Prediction API
- Trained ML Model Deployment
- Input Validation using Pydantic
- Prediction Result Storage

### 🗄 Database Management

- SQLAlchemy ORM
- Database Relationships
- User-Specific Predictions
- Alembic Database Migrations
- Environment-Based Configuration

### ⚡ Backend Development

- FastAPI REST APIs
- Modular Architecture
- Dependency Injection
- Request & Response Validation
- Interactive Swagger Documentation
- ReDoc API Documentation

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- Pydantic

## Database

- SQLAlchemy
- SQLite
- Alembic

## Authentication & Security

- JWT (JSON Web Tokens)
- Passlib
- bcrypt

## Machine Learning

- Scikit-Learn
- Pandas
- NumPy

## Development Tools

- Git
- GitHub
- Virtual Environment

---

# 📂 Project Structure

```text
House_price_prediction_model/
│
├── app/
│   ├── controller.py
│   ├── schemas.py
│   ├── model_loader.py
│   ├── inference.py
│   ├── router.py
│   ├── helpers.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   ├── models_db.py
│   │   ├── settings.py
│   │   └── rough.py
│   │
│   └── user/
│       ├── controller.py
│       ├── models.py
│       ├── dtos.py
│       └── router.py
│
├── models/
│   ├── preprocessing.py
│   ├── train.py
│   ├── training_data_loader.py
│   ├── pipeline.pkl
│   └── dataset/
│       └── house_data.csv
│
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│
├── main.py
├── pipeline.pkl
├── alembic.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone git@github.com:arpitsharmaji/House_price_prediction_model.git
cd House_price_prediction_model
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Application URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

ReDoc Documentation:

```text
http://localhost:8000/redoc
```

---

# 🔐 Authentication Workflow

## Register User

**Endpoint**

```http
POST /user/register
```

Creates a new user account and securely stores a hashed password.

---

## Login User

**Endpoint**

```http
POST /user/login_user
```

Validates user credentials and generates a JWT access token.

---

## Verify Authentication

**Endpoint**

```http
GET /user/is_auth
```

Verifies whether the provided JWT token is valid and returns authenticated user information.

---

# 🏠 House Price Prediction APIs

All task routes require authentication.

## Create Prediction

```http
POST /tasks/create
```

Creates a new house price prediction record.

---

## Get All Predictions

```http
GET /tasks/all_tasks
```

Returns all predictions associated with the authenticated user.

---

## Get Prediction By ID

```http
GET /tasks/one_task/{task_id}
```

Returns a single prediction record.

---

## Update Prediction

```http
PUT /tasks/update_task/{task_id}
```

Updates an existing prediction.

---

## Delete Prediction

```http
DELETE /tasks/delete_task/{task_id}
```

Deletes a prediction record.

---

# 🤖 Machine Learning Workflow

The application uses a trained Scikit-Learn pipeline to predict house prices based on input features.

### Workflow

1. User submits house details.
2. Request is validated using Pydantic schemas.
3. Features are preprocessed.
4. Trained ML pipeline loads.
5. Prediction is generated.
6. Prediction is stored in the database.
7. Response is returned to the client.

---

# 🗄 Database Migration

### Apply Migrations

```bash
alembic upgrade head
```

### Create Migration

```bash
alembic revision --autogenerate -m "migration_name"
```

### Downgrade Migration

```bash
alembic downgrade -1
```

---

# 🔒 Security Features

- JWT Authentication
- Password Hashing with bcrypt
- Protected Endpoints
- User Authorization
- Request Validation
- Secure Credential Storage
- Stateless Authentication
- Dependency-Based Authentication Middleware

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- FastAPI
- REST API Development
- SQLAlchemy ORM
- Alembic Migrations
- JWT Authentication
- Password Hashing
- Authorization
- Machine Learning Model Deployment
- Backend Architecture
- Dependency Injection
- API Security
- Git & GitHub

---

# 🔮 Future Improvements

- Docker Containerization
- GitHub Actions CI/CD
- PostgreSQL Integration
- Redis Caching
- Role-Based Access Control (RBAC)
- MLflow Integration
- Cloud Deployment (AWS/GCP/Azure)
- Monitoring & Logging
- Automated Model Retraining

---

# 👨‍💻 Author

**Arpit Sharma**

Backend Developer | FastAPI Developer | Machine Learning Enthusiast | MLOps Learner

GitHub: https://github.com/arpitsharmaji

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
