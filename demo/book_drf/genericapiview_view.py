from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from books.models import BookInfo
from book_drf.serializer import BookSerializer

# Create your views here.
class Books(GenericAPIView):

    queryset = BookInfo.objects.all()   # Specify the query set data used by the current class view
    serializer_class = BookSerializer   # Specify the serializer used by the current class view
    def get(self, request):
        # Query all book objects
        books = self.get_queryset() # Get all the data in the query set
        ser = self.get_serializer(books, many=True) # Get the serializer object using the specified serializer
        return Response(ser.data)

    def post(self, request):
        # 1. Get Front End Data
        data = request.data
        # 2. Validation Data
        ser = self.get_serializer(data=data)    # Get the serializer object using the specified serializer
        ser.is_valid()
        print(ser.validated_data)
        # 3. Save Data
        # book = BookInfo.objects.create(name=name, pub_date=pub_date)
        ser.save()
        # 4. Return results
        return Response(
            ser.data
        )


class Book(GenericAPIView):
    """Get single and update and delete"""

    def get(self, request):
        book = BookInfo.objects.get(id=1)
        ser = BookSerializer(book)
        return Response(ser.data)


class BookDRFView(GenericAPIView):
    queryset = BookInfo.objects.all()   # Specify the query set data used by the current class view
    serializer_class = BookSerializer   # Specify the serializer used by the current class view

    def put(self, request, pk):
        # 1. Get Front End Data
        data = request.data
        # 2. Validation Data
        # 3. Update Data
        try:
            book = self.get_object()    # Get a specified single data object from a query set
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
