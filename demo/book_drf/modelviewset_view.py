from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.throttling import UserRateThrottle
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

from book_drf.serializer import BookSerializer
from books.models import BookInfo

class PageNum(PageNumberPagination):
    """
    Customizable Pager
    """
    page_size_query_param = 'page_size' # Specify the parameters that control the number of pages per
    max_page_size = 6   # Specify the maximum number of returns per page


class Books(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer
    # Authentication
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    # Permission
    permission_classes = (IsAuthenticated, )
    # Throttling
    # throttle_classes = [UserRateThrottle]
    # throttle_scope = 'uploads'

    # Filter fields
    # filterset_fields = ('name', 'readcount')

    # Specify the sorting method class
    filter_backends = [OrderingFilter]
    # Specify Sort Fields
    ordering_fields = ('id', 'readcount')
    # Specify pagination
    pagination_class = PageNum

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

