# FastAPI Project

## Description

This project is a **FastAPI** application that provides an API for managing API keys with features like generation, validation, and expiration.

## Project Setup

To set up the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mnawaz6935/FastAPI.git
   cd FastAPI
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database and run migrations:**
   Make sure you have **Alembic** configured in your project. To apply the migrations, run:
   ```bash
   alembic upgrade head
   ```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```