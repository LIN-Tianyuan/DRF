from django.views import View
from django.http import JsonResponse
from .models import BookInfo
import json

# Create your views here.
class BooksView(View):
    """
    Get All and Save
    """
    def get(self, request):
        # 1. Get single and update and delete
        books = BookInfo.objects.all()
        # 2. Return book data [{}, {}, {}]
        book_list = []
        for book in books:
            book_list.append(
                {
                    'id': book.id,
                    'name': book.name,
                    'readcount':book.readcount,
                    'commentcount': book.commentcount,
                    'pub_date': book.pub_date
                }
            )
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        # 1. Get Front End Data
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2. Validation Data
        name = data_dict.get('name')
        pub_date = data_dict.get('pub_date')
        if pub_date is None or name is None:
            return JsonResponse({'error': 'Error message'}, status=400)
        # 3. Save Data
        book = BookInfo.objects.create(name=name, pub_date=pub_date)
        # 4. Return results
        return JsonResponse(
            {
                'id': book.id,
                'name': book.name,
                'readcount':book.readcount,
                'commentcount': book.commentcount,
                'pub_date': book.pub_date
            }
        )

class BookView(View):
    """Get single and update and delete"""
    def get(self, request, pk):
        # 1. Query Data Object
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'Error message'}, status=400)
        return JsonResponse(
            {
                'id': book.id,
                'name': book.name,
                'readcount':book.readcount,
                'commentcount': book.commentcount,
                'pub_date': book.pub_date
            }
        )

    def put(self, request, pk):
        # 1. Get Front End Data
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2. Validation Data
        name = data_dict.get('name')
        pub_date = data_dict.get('pub_date')
        if pub_date is None or name is None:
            return JsonResponse({'error': 'Error message'}, status=400)
        # 3. Update Data
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'Error message'}, status=400)
        book.name = name
        book.pub_date = pub_date
        book.save()
        # 4. Return results
        return JsonResponse(
            {
                'id': book.id,
                'name': book.name,
                'readcount':book.readcount,
                'commentcount': book.commentcount,
                'pub_date': book.pub_date
            }
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