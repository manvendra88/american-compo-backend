from django.contrib import admin
from .models import contact_us_table
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'phone_number')

admin.site.register(contact_us_table, ContactUsAdmin)
