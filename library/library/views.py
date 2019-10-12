from django.shortcuts import render
from django.http import HttpResponse

from author.models import Author
from books.models import Book

def add_all(request):
    return render(request,'add.html')

def add(request):
    book_name=request.POST["bname"]
    author_name=request.POST["aname"]
    genre=request.POST["genre"]
    age=request.POST["a_age"]
    style=request.POST["style"]
    # creating a book and an author and linking them #

    Author.objects.create(name=author_name,age=age,style=style)
    a=Author.objects.get(name=author_name).id
    Book.objects.create(name=book_name,genre=genre,author_id=a)

    book_data=Book.objects.filter()
    author_data=Author.objects.filter()

    return render(request,'add.html',{'book_data':book_data,'author_data':author_data})