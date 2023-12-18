1
from django.contrib import admin
from org_backend.models import *
from django.apps import apps

for model in apps.get_app_config('org').models.values():
    admin.site.register(model)