
from django.urls import path

"""
from . import views
urlpatterns = [
    path('books_drf/', views.Books.as_view()),
    path('book_drf/', views.Book.as_view()),
    path('books_drf/<int:pk>/', views.BookDRFView.as_view()),
]
"""

"""
from . import apiview_view
urlpatterns = [
    path('books_drf/', apiview_view.Books.as_view()),
    path('book_drf/', apiview_view.Book.as_view()),
    path('books_drf/<int:pk>/', apiview_view.BookDRFView.as_view()),
]
"""

"""
from . import genericapiview_view
urlpatterns = [
    path('books_drf/', genericapiview_view.Books.as_view()),
    path('book_drf/', genericapiview_view.Book.as_view()),
    path('books_drf/<int:pk>/', genericapiview_view.BookDRFView.as_view()),
]
"""

"""
from . import mixin_view
urlpatterns = [
    path('books_drf/', mixin_view.Books.as_view()),
    path('book_drf/', mixin_view.Book.as_view()),
    path('books_drf/<int:pk>/', mixin_view.BookDRFView.as_view()),
]
"""
"""
from . import childmixin_view
urlpatterns = [
    path('books_drf/', childmixin_view.Books.as_view()),
    path('book_drf/', childmixin_view.Book.as_view()),
    path('books_drf/<int:pk>/', childmixin_view.BookDRFView.as_view()),
]
"""
"""
from . import viewset_view
urlpatterns = [
    path('books_drf/', viewset_view.Books.as_view({'get': 'list', 'post': 'create'})),
    # path('book_drf/', viewset_view.Book.as_view()),
    path('books_drf/<int:pk>/', viewset_view.BookDRFView.as_view({'put': 'update'})),
]
"""

from . import genericviewset_view
urlpatterns = [
    path('books_drf/', genericviewset_view.Books.as_view({'get': 'list', 'post': 'create'})),
    # path('book_drf/', viewset_view.Book.as_view()),
    path('books_drf/<int:pk>/', genericviewset_view.BookDRFView.as_view({'put': 'update'})),
]