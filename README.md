# 🛒 ShopEase E-Commerce System

![Build Status](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions/workflows/ci_pipeline.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)

**ShopEase** is a robust, scalable e-commerce backend built with **Python Flask**. It features a modular MVC architecture, secure user authentication, and a RESTful API designed for mobile integration. The project follows modern DevOps practices, including **Docker containerization** and an automated **CI/CD pipeline** via GitHub Actions.

---

## ✨ Key Features

* **🔐 User Authentication:** Secure registration and login with session management.
* **🛍️ Product Management:** Browse, search, and filter products dynamically.
* **🛒 Shopping Cart:** Persistent cart functionality using session storage.
* **📦 Order System:** Complete checkout workflow with order history.
* **📱 REST API:** A dedicated JSON endpoint (`/api/products`) ready for Android/Mobile integration.
* **🏗️ Design Patterns:** Implements **Singleton** (Database) and **Factory** (App Initialization) patterns.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask (Blueprints)
* **Architecture:** Model-View-Controller (MVC)
* **Database:** CSV-based persistence (Simulated Relational DB)
* **Testing:** Pytest (Unit Tests)
* **DevOps:** Docker, Docker Compose, GitHub Actions (CI/CD)

---

## 🚀 Getting Started

You can run this project in two ways: using **Docker** (recommended) or **Python**.

### Option 1: Run with Docker (Recommended)
This method ensures the app runs in an isolated container with all dependencies installed automatically.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd "implementation phase"
    ```

2.  **Start the application:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the App:**
    * **Web Store:** [http://localhost:5000](http://localhost:5000)
    * **JSON API:** [http://localhost:5000/api/products](http://localhost:5000/api/products)

### Option 2: Run Manually (Python)

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Server:**
    ```bash
    python run.py
    ```

---

## 🧪 Testing & Quality Assurance

This project maintains high code quality through automated testing.

* **Unit Tests:** 6 comprehensive tests covering Routing, Auth, and Blueprints.
* **CI/CD:** Every push to `main` triggers a GitHub Action workflow that:
    1.  Sets up a Python environment.
    2.  Runs all unit tests.
    3.  Builds the Docker image to ensure deployability.

To run tests manually:
```bash
python -m pytest

📂 Project Structure

implementation phase/
├── .github/workflows/    # CI/CD Pipeline Configuration
├── project_code/
│   ├── controllers/      # Route logic (Blueprints)
│   ├── models/           # Data classes
│   ├── repositories/     # Data access layer (CSV handling)
│   ├── templates/        # HTML Frontend (Jinja2)
│   └── __init__.py       # App Factory
├── tests/                # Unit Tests
├── Dockerfile            # Container definition
├── docker-compose.yml    # Container orchestration
├── requirements.txt      # Python dependencies
└── run.py                # Application entry point


🔌 API Reference
Get All Products Returns a list of all products in JSON format.

URL: /api/products

Method: GET

Success Response:

[
  {
    "id": "1",
    "name": "Laptop",
    "price": 999.99,
    "image": "laptop.jpg"
  }
]
