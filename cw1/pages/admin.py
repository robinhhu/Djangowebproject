from django.contrib import admin

# Register your models here.
from .models import Module, Professor,Rating, User
admin.site.register([Module, Professor, Rating, User])


