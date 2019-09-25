import graphene

import books.schema

class Query(books.schema.Query,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)