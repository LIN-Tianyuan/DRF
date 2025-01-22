# DRF
DRF(Django Restful Framework) 
## 1. Non-separation Quick Build
```bash
python3 -m venv django-py3
source django-py3/bin/activate
pip3 install django

django-admin startproject demo
cd demo
python3 manage.py startapp book
```
```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book.apps.BookConfig'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'books',
        'USER': 'root',
        'PASSWORD': 'alex4869',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}
```
```python
# demo/__init__.py
from pymysql import install_as_MySQLdb

install_as_MySQLdb()
```
```python
# demo/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('book.urls'))
]
```
```python
# book/urls.py
from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view())
]
```
```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <div><h1>{{ name }}</h1></div>
</body>
</html>
```

