from django.contrib import admin
from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    """customize display of fields in the UserAccount model"""
    list_display = ['id', 'name', 'email']
    list_display_links = ['id', 'name', 'email']
    search_fields = ['name']
    list_per_page = 25

admin.site.register(UserAccount, UserAccountAdmin)