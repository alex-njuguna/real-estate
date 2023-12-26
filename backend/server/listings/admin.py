from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    """customize viewing the listing model in the admin panel"""
    list_display = ['realtor', 'title', 'address', 'location', 'county', 'sale_type', 'size', 'price']
    list_display_links = ['realtor', 'title', 'address']
    search_fields = ['realtor', 'price', 'county']
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)