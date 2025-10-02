# Ecommerce API  

A RESTful API for managing an ecommerce platform, built with **Django Rest Framework (DRF)** and **JWT authentication**.  
This API allows users to register, browse products, leave reviews, and manage their cart & orders.  

---

## Features  

- **User Management**
  - User registration with secure password hashing.
  - JWT authentication for login & protected endpoints.

- **Products & Categories**
  - CRUD for products and categories.
  - Stock management with dynamic available stock calculation.

- **Cart & Orders**
  - Add products to cart (`CartItem`).
  - Auto-create a pending order for each user.
  - Automatic total price recalculation on cart changes.
  - Order history with status tracking (`pending`, `processing`, `shipped`, `delivered`, `cancelled`).

- **Reviews & Ratings**
  - Users can rate and review products (1–5 stars).
  - Each user can review a product only once.
  - Filter reviews by product, category, or rating.

---

## Tech Stack  

- **Backend:** Django, Django Rest Framework  
- **Authentication:** JWT (`djangorestframework-simplejwt`)  
- **Filtering:** django-filter  
- **Database:** SQLite (default) or configurable to Postgres/MySQL  

---

## Installation & Setup  

### 1. Clone the repository  

```bash
git clone https://github.com/your-username/ecommerce-api.git
cd ecommerce-api

python -m venv venv
source venv/bin/activate   # On Linux / Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

API will be available at:
http://127.0.0.1:8000/

```
### 1. Authentication

This project uses JWT Authentication

```bash
POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}

POST /api/token/refresh/
{
  "refresh": "your_refresh_token"
}

Authorization: Bearer <your_access_token>
```
