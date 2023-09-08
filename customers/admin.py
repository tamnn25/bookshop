from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("email","first_name","last_name")

admin.site.register(User, UserAdmin)