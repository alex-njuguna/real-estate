from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    # customized look of the Contact model on the admin panel
    list_display = ['id', 'name', 'email', 'subject']
    list_display_links = ['id', 'name', 'subject']
    search_fields = ['name', 'email', 'subject']
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
