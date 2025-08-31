# E-commerce Application

## Project Overview
This project is a full-stack e-commerce web application built using **Django**, **Django REST Framework**, and **Bootstrap**.  
It provides a complete solution for managing products, categories, and user orders, with a focus on a clean, functional user interface.

---

## Key Features
- **User Authentication**  
  Secure user registration, login, and logout functionality.

- **Dynamic Profile Management**  
  Authenticated users can view and update their profile information.

- **Product Catalog**
  - Browse all products on the main grid.
  - View detailed information for each product.

- **Product Search and Filtering**  
  A robust search bar allows users to find products by name, description, or category.

- **Product Management (Admin-only)**
  - Create new products.
  - Edit existing product details.
  - Delete products from the catalog.

- **Order Management**
  - View a list of your placed orders.
  - Delete orders from your history.

- **Responsive UI**  
  The application is styled with Bootstrap to ensure it is usable on both desktop and mobile devices.

---

## Technology Stack
- **Backend**: Django, Django REST Framework  
- **Frontend**: Django Templates, HTML, CSS, JavaScript, Bootstrap  
- **Database**: SQLite (default)

---

## Getting Started

### Prerequisites
- Python 3.8 or higher  
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/atiddl/Project-repo.git
   cd Project-repo
   cd ecommerce_api
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt

Note: If you don't have a requirements.txt file, create one with:

Django==5.2
djangorestframework==3.15.1
django-filter==24.2

4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser

6. Run the development server:
   ```bash
   python manage.py runserver


The application will now be running at:

👉 http://127.0.0.1:8000/

| Endpoint              | HTTP Method | Description                              |
| --------------------- | ----------- | ---------------------------------------- |
| `/api/products/`      | GET         | List all products.                       |
| `/api/products/<id>/` | GET         | Retrieve a single product.               |
| `/api/products/`      | POST        | Create a new product (authenticated).    |
| `/api/products/<id>/` | PUT/PATCH   | Update a product (authenticated).        |
| `/api/products/<id>/` | DELETE      | Delete a product (authenticated).        |
| `/api/orders/`        | GET         | List user's orders (authenticated).      |
| `/api/orders/<id>/`   | DELETE      | Delete a specific order (authenticated). |
| `/api/users/`         | GET         | List all users.                          |
| `/api/categories/`    | GET         | List all product categories.             |

License

This project is licensed under the MIT License.
