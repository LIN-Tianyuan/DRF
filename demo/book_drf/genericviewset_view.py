from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from books.models import BookInfo
from book_drf.serializer import BookSerializer

# Create your views here.
class Books(GenericViewSet):
    queryset = BookInfo.objects.all()   # Specify the query set data used by the current class view
    serializer_class = BookSerializer   # Specify the serializer used by the current class view

    def list(self, request):
        # Query all book objects
        books = self.get_queryset()
        ser = self.get_serializer(books, many=True)
        return Response(ser.data)

    def create(self, request):
        # 1. Get Front End Data
        data = request.data
        # 2. Validation Data
        ser = self.get_serializer(data=data)
        # ser.is_valid(raise_exception=True)  # Validation Methods
        ser.is_valid()
        print(ser.validated_data)
        # 3. Save Data
        # book = BookInfo.objects.create(name=name, pub_date=pub_date)
        ser.save()
        # 4. Return results
        return Response(
            ser.data
        )

class BookDRFView(GenericViewSet):
    def update(self, request, pk):
        # 1. Get Front End Data
        data = request.data
        # 2. Validation Data
        # 3. Update Data
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'Error message'}, status=400)
        ser = BookSerializer(book, data=data)
        ser.is_valid()
        ser.save()
        # 4. Return results
        return Response(
            ser.data
        )

    def delete(self, request ,pk):
        # 1. Query Data Object
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return Response({'error': 'Error message'}, status=400)
        book.is_delete = True
        book.save()
        return Response({})

class Book(GenericViewSet):
    """Get single and update and delete"""

    def get(self, request):
        book = BookInfo.objects.get(id=1)
        ser = BookSerializer(book)
        return Response(ser.data)
