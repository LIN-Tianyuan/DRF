from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from book_drf.serializer import BookSerializer
from books.models import BookInfo


class Books(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BookSerializer
        else:
            return BookSerializer

    @action(methods=['get'], detail=True)
    def lastdata(self, request, pk):
        print(self.action)
        book = BookInfo.objects.get(id=pk)
        ser = BookSerializer(book)
        return Response(ser.data)

