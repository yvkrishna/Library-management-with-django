from django.urls import path
from . import views

urlpatterns = [
    path('author/',views.home,name="home"),
    path('add_auth/',views.add_auth,name="add_auth"),
    path('add_auth/authadd',views.authadd,name="authadd")
]