from django.urls import path

from todos import views


urlpatterns = [
    path('<int:pk>/', views.DetailTodo.as_view()),
    path('', views.ListTodo.as_view())
]