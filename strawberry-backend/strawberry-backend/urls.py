from django.contrib import admin
from django.urls import path

#Cross Site Request Forgery protection middleware. See https://docs.djangoproject.com/en/4.2/ref/csrf/
from django.views.decorators.csrf import csrf_exempt
from org import schema

#Strawberry
from strawberry.django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    
]