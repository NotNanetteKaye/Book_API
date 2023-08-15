from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

@api_view(['GET', 'POST'])
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)