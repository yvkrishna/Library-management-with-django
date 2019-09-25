from django.urls import path
from . import views

urlpatterns = [
    path('author/',views.home,name="home"),
]