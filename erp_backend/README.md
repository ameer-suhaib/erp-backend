# ERP Backend - User & Role Management System

This is the backend implementation for an ERP system that supports role-based access control (RBAC) using **Django** and **Django REST Framework** with **JWT authentication**.

---

## Features

- User registration and login using JWT
- Role-based access control (Admin, Manager, Employee)
- Admin can add/edit/delete users
- Manager can view all employees
- Employee can only view their own profile
- PostgreSQL/MySQL supported
- Secured API endpoints

---

## Tech Stack

- Python 3.12
- Django
- Django REST Framework (DRF)
- djangorestframework-simplejwt
- PostgreSQL
- CORS headers

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ameer-suhaib/erp-backend.git
cd erp-backend
