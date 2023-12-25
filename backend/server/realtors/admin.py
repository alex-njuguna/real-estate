from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    """fields to display in the admin panel for the Realtor model"""
    list_display = ['id', 'name', 'phone', 'email', 'date_hired']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)


