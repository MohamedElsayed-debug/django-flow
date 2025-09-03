# django-flow

**Django Flow** is an open-source project to build an automation platform (similar to [n8n]) using **Django + Python**.  
The goal is to connect different tools and tasks (e.g., posting to Facebook, fetching data from APIs, sending emails...) and automate workflows with ease.

-----

## Features (current)
- Facebook posting tool using access tokens directly.
- Scalable design for adding new integrations (Twitter, Instagram, WhatsApp, etc.).

-----

## Requirements
- Python 3.11+
- Django 5+
- Additional libraries depending on the integration (to be listed later).

---

## Getting Started
```bash
git clone https://github.com/username/django-flow.git
cd django-flow
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
