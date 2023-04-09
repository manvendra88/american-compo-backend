from django.contrib import admin
from .models import about_us_table
# Register your models here.

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('image', 'text')

admin.site.register(about_us_table, AboutUsAdmin)
