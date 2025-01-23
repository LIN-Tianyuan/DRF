from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('books_drf/', views.Books.as_view()),
    path('book_drf/', views.Book.as_view()),
    path('books_drf/<int:pk>/', views.BookDRFView.as_view()),
]