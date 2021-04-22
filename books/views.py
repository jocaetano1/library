from django.shortcuts import render
from books.models import Book


def book_list_view(request, **kwargs):
    template_name = 'books/book_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template_name, context)