from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.serializers import Serializer

from books.models import Book

from api.serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookTestAPIView(APIView):
    
    def get(self, request, format=None):
        books = Book.objects.all()
        data = list()
        for book in books:
            data.append({
                'id': book.id,
                'author': book.author.id,
                'img': book.author.picture.url,
                'title': book.title,
                'subtitle': book.subtitle
            })
        from json import dumps
        data = dumps(data)
        return Response(data=data)
    