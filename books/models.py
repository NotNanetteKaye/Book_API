from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    book_description = models.CharField(max_length=500)
