from django.contrib import admin

# Register your models here.
from .models import Department, Location

admin.site.register(Department)
admin.site.register(Location)
