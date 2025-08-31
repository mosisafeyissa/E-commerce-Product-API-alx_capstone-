E-commerce Product API

A full-stack e-commerce application built with Django and Django REST Framework, designed to provide a functional online store with product management, user authentication, and order tracking. This project is ideal for small businesses or as a learning project for full-stack development.

Table of Contents

Project Overview

Features

Technologies Used

Installation

Usage

API Endpoints

Contributing

License

Project Overview

This application allows users to:

Register and log in to their account

Browse available products in a grid

Search for products by name

Add, edit, and delete products (admin functionality)

View and manage personal orders

Update profile information

It demonstrates core e-commerce functionality while using Django’s robust backend features, including authentication, authorization, and RESTful API endpoints.

Features

User Authentication: Registration, login, logout, and profile management

Product Management: Add, edit, delete, and view products

Search Functionality: Filter products by name

Order Management: View order history and manage orders

Responsive UI: Uses Bootstrap for a clean and simple interface

Technologies Used

Python 3.13

Django 5.2.5

Django REST Framework

SQLite (default, can be changed to MySQL/PostgreSQL)

Bootstrap 5

HTML & CSS

Installation

Clone the repository

git clone https://github.com/mosisafeyissa/E-commerce-Product-API-alx_capstone-.git
cd E-commerce-Product-API-alx_capstone-


Create and activate a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Create a superuser (for admin access)

python manage.py createsuperuser


Run the development server

python manage.py runserver


Open your browser and go to: http://127.0.0.1:8000/

Usage

Register a new user or log in with an existing account

Browse products on the homepage

Search products using the search bar

Add/Edit/Delete products (requires login with proper permissions)

View order history under 'My Orders'

Update profile through the profile page

API Endpoints (Example)

This section can be expanded depending on your API implementation

Endpoint	Method	Description
/api/products/	GET	List all products
/api/products/<id>/	GET	Get a single product by ID
/api/products/create/	POST	Create a new product (admin only)
/api/products/<id>/update/	PUT/PATCH	Update product (admin only)
/api/products/<id>/delete/	DELETE	Delete product (admin only)
Contributing

Contributions are welcome! To contribute:

Fork this repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m 'Add feature')

Push to the branch (git push origin feature/your-feature)

Open a Pull Request

License

This project is licensed under the MIT License. See the LICENSE
 file for details.