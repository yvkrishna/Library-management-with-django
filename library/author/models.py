from django.db import models

# Create your models here.
class Author(models.Model):
    id=models.AutoField(primary_key=true)
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    style=models.CharField(max_length=100)