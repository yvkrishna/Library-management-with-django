from django.db import models
from author.models import Author
# Create your models here.
class Book(models.Model):
    type="Book"
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    author_id=models.CharField(max_length=100)