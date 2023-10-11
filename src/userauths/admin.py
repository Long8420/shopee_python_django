from django.contrib import admin
from userauths.models import User
# Register your models herecl

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

admin.site.register(User, UserAdmin)
