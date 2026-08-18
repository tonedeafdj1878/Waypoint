# Waypoint 🏔️

> Your ultimate hiking and trail management companion.

[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)

---

## 🚀 Features

- **Trail Reporting & Management:** Submit detailed reports for new trails, including distance, elevation gain, difficulty levels, and personal notes.
- **Dynamic Home Dashboard:** View an up-to-date list of all reported trails pulled directly from the database.
- **Django Admin Integration:** Fully configured administrative backend for managing users, permissions, and trail records securely.
- **Automated Test Suite:** Comprehensive unit tests covering model constraints, URL routing, and HTTP request handling.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Version Control:** Git & GitHub

---

## 📦 Getting Started Locally

1. Clone the Repository

git clone [https://github.com/tonedeafdj1878/Waypoint.git](https://github.com/tonedeafdj1878/Waypoint.git)
cd Waypoint

2. Create and Activate a Virtual Environment
   python -m venv env

3. Install Dependencies

pip install -r requirements.txt

4. Run Database Migrations

python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (Optional for Admin Access)

python manage.py createsuperuser

6. Run the Development Server

python manage.py runserver

Running Tests

To execute the automated unit test suite:

python manage.py test
