import graphene
from graphene_django import DjangoObjectType

from .models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    booksid = graphene.Field(BookType,
                              authorId=graphene.String(),
                              name=graphene.String(),
                              genre=graphene.String())
    def resolve_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_booksid(self, info, **kwargs):
        name = kwargs.get('name')

        if name is not None:
            return Book.objects.get(name=name)

        return None