import graphene

from org_backend.schema  import Query as OrgQuery;
from blog.schema  import Query as BlogQuery; 


class Query(OrgQuery, BlogQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

# class Mutation(org_app.schema.Mutation, blog_app.schema.Mutation, graphene.ObjectType):
#   pass
#schema = graphene.Schema(query=Query, mutation=Mutation)