from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.home,name="home"),
    path('add_books/addbook',views.addbooks,name="addbooks"),
    path('add_books/',views.add_books,name="add_books")
]