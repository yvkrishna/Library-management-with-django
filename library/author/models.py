from django.db import models

# Create your models here.
class Author(models.Model):
    type="Author"
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=100)
    style=models.CharField(max_length=100)