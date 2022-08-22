from django.contrib import admin
from django.urls import path
from book_api.views import book, book_create, book_list

urlpatterns = [
    path('', book_create),
    path('list/', book_list),
    path('<int:pk>', book)
]
