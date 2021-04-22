from django.urls import path
from api import views

app_name = 'api'


urlpatterns = [
    path('', views.BookTestAPIView.as_view(), name='list'),
]

"""
        {% if books %}
        <h1>All Books</h1>
        {% for book in books %}
            <ul>
                <li>Title: {{ book.title }}</li>
                <li>Subtitle: {{ book.subtitle }}</li>
                <li>Author: {{ book.author }}</li>
                <li>ISBN: {{ book.isbn }}</li>
            </ul>
        {% empty %}
        <p>No books avaliable.</p>
        {% endfor %}
        {% endif %}    

"""