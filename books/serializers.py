from rest_framework import serializers
from . import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'book_description']