from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from books.models import BookInfo
from book_drf.serializer import BookSerializer

# Create your views here.
class Books(ListCreateAPIView):
    throttle_scope = 'contacts'
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer
    queryset = BookInfo.objects.all()   # Specify the query set data used by the current class view
    serializer_class = BookSerializer   # Specify the serializer used by the current class view


class BookDRFView(RetrieveUpdateDestroyAPIView):
    queryset = BookInfo.objects.all()   # Specify the query set data used by the current class view
    serializer_class = BookSerializer   # Specify the serializer used by the current class view




class Book(GenericAPIView):
    """Get single and update and delete"""

    def get(self, request):
        book = BookInfo.objects.get(id=1)
        ser = BookSerializer(book)
        return Response(ser.data)
