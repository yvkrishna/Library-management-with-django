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


class createBook(graphene.Mutation):
    id=graphene.Int()
    name=graphene.String()
    genre=graphene.String()
    author_id=graphene.String()

    class Arguments:
        name=graphene.String()
        genre=graphene.String()
        author_id=graphene.String()

    def mutate(self, info, name, genre, author_id):
        Book.objects.create(name=name,genre=genre,author_id=author_id)

        return createBook(name=name,genre=genre,author_id=author_id)


class Mutation(graphene.ObjectType):
    create_book = createBook.Field()