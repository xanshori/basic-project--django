from django.contrib import admin
from .models import Profile
# Register your models here.
class AdminShow(admin.ModelAdmin):
    readonly_fields= [
        'slug'
    ]

admin.site.register(Profile,AdminShow)