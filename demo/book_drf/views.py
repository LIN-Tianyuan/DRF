from django.http import JsonResponse
from django.views import View
from books.models import BookInfo
from .serializer import BookSerializer
import json

# Create your views here.
class Books(View):
    def get(self, request):
        # Query all book objects
        books = BookInfo.objects.all()
        ser = BookSerializer(books, many=True)
        return JsonResponse(ser.data, safe=False)

    def post(self, request):
        # 1. Get Front End Data
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2. Validation Data
        ser = BookSerializer(data=data_dict)
        # ser.is_valid(raise_exception=True)  # Validation Methods
        ser.is_valid()
        print(ser.validated_data)
        # 3. Save Data
        # book = BookInfo.objects.create(name=name, pub_date=pub_date)
        ser.save()
        # 4. Return results
        return JsonResponse(
            ser.data
        )


class Book(View):
    """Get single and update and delete"""
    def get(self, request):
        book = BookInfo.objects.get(id=1)
        ser = BookSerializer(book)
        return JsonResponse(ser.data)


class BookDRFView(View):
    def put(self, request, pk):
        # 1. Get Front End Data
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2. Validation Data
        # 3. Update Data
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'Error message'}, status=400)
        ser = BookSerializer(book, data=data_dict)
        ser.is_valid()
        ser.save()
        # 4. Return results
        return JsonResponse(
            ser.data
        )

    def delete(self, request ,pk):
        # 1. Query Data Object
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'Error message'}, status=400)
        book.is_delete = True
        book.save()
        return JsonResponse({})
