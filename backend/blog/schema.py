from __future__ import unicode_literals
import graphene
from graphene_django import DjangoObjectType
from blog.models import BlogPostPage

from django.db import models

class ArticleNode(DjangoObjectType):
    class Meta:
        model = BlogPostPage
        only_fields = ['title', 'date', 'intro', 'body']


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleNode)

    @graphene.resolve_only_args
    def resolve_articles(self):
        return BlogPostPage.objects.live()

schema = graphene.Schema(query=Query)