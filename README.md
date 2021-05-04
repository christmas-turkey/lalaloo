# Introduction

LaLaLoo is a video service for uploading your videos and watch other people's videos

# Usage

### Create virtual environment (optional)

```
python -m venv venv
```

```
.\venv\Scripts\activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Create database migrations

```
python manage.py makemigrations
```

```
python manage.py migrate
```

### Run the server

```
python manage.py runserver
```

# Custom commands

There is one availible custom command that deletes absolutely all videos from the website

```
python manage.py delete-videos
```