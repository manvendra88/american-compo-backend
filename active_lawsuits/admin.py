from django.contrib import admin
from .models import active_law_table
# Register your models here.

class ActiveLawsuit(admin.ModelAdmin):
    list_display = ('name', 'text')

admin.site.register(active_law_table, ActiveLawsuit)
