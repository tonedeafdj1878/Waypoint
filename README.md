# Waypoint 🏔️

Waypoint is a web application built with **Django** designed for hikers and outdoor enthusiasts to track, manage, and share trail reports.

---

## Features

- **Trail Management:** Submit and view detailed hiking reports including distance, elevation gain, difficulty levels, and personal notes.
- **Responsive Styling:** Integrated CSS static files for a clean, user-friendly interface across home, report, and success views.
- **Django Admin Integration:** Fully managed data administration via the built-in Django admin panel.
- **Robust Testing:** Includes automated unit tests and object-oriented validation scripts.

---

## Project Structure

```text
Waypoint/
│
├── core/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   └── core/
│   │       ├── home.html
│   │       ├── report.html
│   │       └── report_success.html
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── waypoint/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── test_hierarchy.py
└── README.md
```
