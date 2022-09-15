from re import I
from django.contrib import admin
from .models import Product
# Register your models here.
class AdminOnly(admin.ModelAdmin):
    readonly_fields=[
        'create',
        'update',
        'slug',
    ]
admin.site.register(Product,AdminOnly)