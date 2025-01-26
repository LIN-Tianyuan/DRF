from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin

from books.models import BookInfo
from book_drf.serializer import BookSerializer

# Create your views here.
class Books(GenericAPIView, CreateModelMixin, ListModelMixin):

    queryset = BookInfo.objects.all()   # Specify the query set data used by the current class view
    serializer_class = BookSerializer   # Specify the serializer used by the current class view

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Book(GenericAPIView):
    """Get single and update and delete"""

    def get(self, request):
        book = BookInfo.objects.get(id=1)
        ser = BookSerializer(book)
        return Response(ser.data)


class BookDRFView(GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = BookInfo.objects.all()   # Specify the query set data used by the current class view
    serializer_class = BookSerializer   # Specify the serializer used by the current class view

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request ,pk):
        # 1. Query Data Object
        return self.destroy(request, pk)