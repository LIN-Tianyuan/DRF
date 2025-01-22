from . import views
from django.urls import path

urlpatterns = [
    # path('books', views.IndexView.as_view()),
    path('books/', views.BooksView.as_view()),
    path('books/<int:pk>/', views.BookView.as_view())
]