from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status
from rest_framework.response import Response

from django.db import DatabaseError

def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is None:
        view = context['view']
        if isinstance(exc, DatabaseError):
            print('[%s]: %s' % (view, exc))
            response = Response({'detail': 'Internal server error'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response