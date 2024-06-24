# My Django Project

## Description

My Django Project is a web application that allows users to manage books in a library. It provides CRUD operations for books, user authentication, and a RESTful API for external access.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/taqim2708/library.git
cd library
```
3. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Apply database migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Open your browser and navigate to `http://localhost:8000/`.
