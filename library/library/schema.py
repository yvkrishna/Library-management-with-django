import graphene
import author.schema
import books.schema

class Query(author.schema.Query,books.schema.Query,graphene.ObjectType):
    pass

class Mutation(author.schema.Mutation, books.schema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)