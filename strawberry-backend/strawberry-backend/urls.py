from django.contrib import admin
from django.urls import path

#Cross Site Request Forgery protection middleware. See https://docs.djangoproject.com/en/4.2/ref/csrf/
from django.views.decorators.csrf import csrf_exempt
 

#Strawberry
from strawberry.django.views import GraphQLView
from org.schema  import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(schema=schema)),
]
    


