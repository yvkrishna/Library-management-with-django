from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
# Create your views here.
def home(request):
    return HttpResponse('hello vedha krishna author')


def add_auth(request):
    return render(request,'addauthor.html')

def authadd(request):
    name=request.POST['aname']
    age=request.POST['a_age']
    style=request.POST['style']

    Author.objects.create(name=name,age=age,style=style)
    author_data=Author.objects.filter()
    return render(request,'addauthor.html',{'author_data':author_data})
