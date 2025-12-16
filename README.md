# 📝 Django To-Do List

A simple, beautiful to-do list application built with Django.

## Features

- ✅ Add new tasks
- ✅ Mark tasks as complete/incomplete
- ✅ Delete tasks
- ✅ Beautiful, responsive UI
- ✅ SQLite database

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/hasib41/to-do-list-django.git
cd to-do-list-django

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create admin user (optional)
python manage.py createsuperuser

# 7. Start the server
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## Project Structure

```
to-do-list-django/
├── manage.py               # Django CLI
├── requirements.txt        # Dependencies
├── db.sqlite3             # Database (auto-created)
│
├── todo_project/          # Project settings
│   ├── settings.py
│   └── urls.py
│
└── tasks/                 # Tasks app
    ├── models.py          # Task model
    ├── views.py           # View functions
    ├── forms.py           # Task form
    ├── urls.py            # URL routes
    └── templates/
        └── tasks/
            └── task_list.html
```

## Tech Stack

- Python 3.12
- Django 6.0
- SQLite
- HTML/CSS

## License

MIT
