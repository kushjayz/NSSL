# NSSL

This repository is for Sri Lanka Nichiren Shoshu meditation center

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django.

```bash
python -m pip install Django
```


## Setting up
Perform migrations

```bash
python manage.py makemigrations
python manage.py migrate
```


Create super admin

```bash
python manage.py createsuperuser
### Enter username and password and create superuser
### The user can login to the Django superadmin terminal via 127.0.0.1:8000/admin/
### It will require to initially add an admin user
### via the superadmin terminal to login to the application
```

Start server
```bash
python manage.py startserver
```
