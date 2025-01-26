from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from book_drf.serializer import BookSerializer
from books.models import BookInfo


class Books(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer

