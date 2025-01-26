from demo.book_drf.serializer import BookSerializer

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

## 2. DRF
```bash
pip install djangorestframework
```
```python
INSTALLED_APPS = [
    ...,
    'rest_framework'
]
```
## 3. Serializer
 - Define the Serializer
 - Nested serialization returns
   - PrimaryKeyRelatedField
   - StringRelatedField
   - Define the serializer separately
 - Use in the view
   - ser=BookSerializer(book)   many=True
   - ser.data
## 4. Deserialization
   - Validation
     - Field option validation
       - max_length
       - min_length
       - max_value
       - min_value
       - default
       - required
       - read_only(Fields are only returned for serialization and are no longer validated)
       - write_only(Fields only participate in deserialization and are no longer returned front-end)
     - Custom Method Validation
       - Single field validation
       ```python
       def validate_name(self, value):
          if value == 'python':
              raise serializers.ValidationError("The title of the book can't be Python.")
          return value
       ```
       - Multiple field validation
        ```python
        def validate(self, attrs):
          if attrs['readcount'] > attrs['commentcount']:
              raise serializers.ValidationError("Read more than commented.")
          return attrs
        ```
       - Validate in view
        ```python
        ser=BookSerializer(data=data_dict)
        ser.isvalid()
        ser.errors   # View Authentication Status Information
        ser.validated_data   # Get validated field data
        ```
   - Save Update
     - save
       - create
     - update
       - update
     - Call Save Updates in a View
       - save()
## 5. Model Class Serializer(ModelSerializer)
Automatic generation of serializer fields

Implemented create and update

Generate unique judgment validation methods
## 6. View class
### 6.1 Two basic class views
#### 6.1.1 APIView
 - Inherit Django's View class
   - Permissions
   - Authentication
   - Flow limiting
#### 6.1.2 GenericAPIView
 - Inherited from APIView class
   - Pagination
   - Filter Sort
   - Specifying query set
     ```python
     books = Book.objects.all()
     for book in books:
        print(book.name)
     ```
     ```python
     queryset = ...(queryset)
     ```
   - Specifying the serializer
     - serializer_class=...(serializer)
### 6.2 Five Expansion Classes(Use with GenericAPIView)
 - ListModelMixin
   - Get multiple data objects
 - CreateModelMixin
   - Save data
 - RetrieveModelMixin
   - Get single data object
 - UpdateModelMixin
   - Update data
 - DestroyModelMixin
   - Delete data
### 6.3 SubClasses of expansion class
## 7. View Collection 
 - 1. Route Matching Rules
 - 2. Methods defined in a view are no longer defined as requested
### 7.1 Two basic view sets
 - ViewSet
   - Inherited from APIView
 - GenericViewSet
   - Inherited from GenericAPIView
### 7.2 Two extended view sets
 - ModelViewSet
   - Inherited from GenericAPIView
   - Inherited from five extension classes
 - ReadOnlyModelViewSet
   - Inherited from GenericAPIView
   - Inherited from ListModelMixin
   - Inheried from RetrieveModelMixin
 - The method of automatic routing generation must be used in conjunction with a view set.