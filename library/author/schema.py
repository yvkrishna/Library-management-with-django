import graphene
from graphene_django import DjangoObjectType

from .models import Author
from books.models import Book

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        

class Query(graphene.ObjectType):

    authors = graphene.List(AuthorType)

    authorid = graphene.Field(AuthorType,
                              name=graphene.String(),
                              age=graphene.String(),
                              style=graphene.String())



    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_authorid(self, info, **kwargs):
        name = kwargs.get('name')

        if name is not None:
            return Author.objects.get(name=name)

        return None


class createAuthor(graphene.Mutation):
    id=graphene.Int()
    name=graphene.String()
    age=graphene.String()
    style=graphene.String()

    class Arguments:
        name=graphene.String()
        age=graphene.String()
        style=graphene.String()

    def mutate(self, info, name, age, style):
        Author.objects.create(name=name,age=age,style=style)

        return createAuthor(name=name,age=age,style=style)


class Mutation(graphene.ObjectType):
    create_author = createAuthor.Field()
