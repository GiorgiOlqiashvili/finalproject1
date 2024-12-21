# Book Lending Service API

A Django-based RESTful API for a book lending service where users can offer and borrow books for free. Non-registered users can browse books, while registered users can add books, manage their listings, and handle borrowing requests.

---

## Features

- **User Authentication**: Registration and login with email-based authentication.
- **Book Management**: Add, update, delete, and view books.
- **Filtering**: Filter books by genre, author, condition, etc.
- **Auxiliary Resources**: Manage authors, genres, conditions, and book-related details.
- **Book Pickup Details**: Specify the location for picking up books.
- **Owner Decision**: Owners can approve or reject book borrowing requests.

---

## Technology Stack

- **Backend Framework**: Django + Django REST Framework
- **Authentication**: Djoser with token-based authentication
- **Database**: PostgreSQL/SQLite (development)
- **Documentation**: Swagger (via `drf-yasg`)
- **Containerization**: Docker & Docker Compose (optional, for deployment)

---

## Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/giorgiolqiashvili/book-lending-service.git
cd book-lending-service

pip install -r requirements.txt
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

