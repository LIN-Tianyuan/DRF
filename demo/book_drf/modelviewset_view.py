from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.throttling import UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend

from book_drf.serializer import BookSerializer
from books.models import BookInfo


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
    filterset_fields = ('name', 'readcount')


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

