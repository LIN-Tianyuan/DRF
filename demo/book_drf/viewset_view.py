from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from books.models import BookInfo
from book_drf.serializer import BookSerializer

# Create your views here.
class Books(ViewSet):
    def list(self, request):
        print(request.query_params)
        # Query all book objects
        books = BookInfo.objects.all()
        ser = BookSerializer(books, many=True)
        return Response(ser.data)

    def create(self, request):
        # 1. Get Front End Data
        data = request.data
        # 2. Validation Data
        ser = BookSerializer(data=data)
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

class BookDRFView(ViewSet):
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

class Book(ViewSet):
    """Get single and update and delete"""

    def get(self, request):
        book = BookInfo.objects.get(id=1)
        ser = BookSerializer(book)
        return Response(ser.data)
