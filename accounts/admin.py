from django.contrib import admin
from .models import User, Profile


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'is_superuser', 'is_staff', 'is_active', 'password']


class ProfileAdmin(admin.ModelAdmin):
    llist_display = ['username', 'first_name', 'last_name']


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
