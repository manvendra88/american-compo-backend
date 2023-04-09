from django.contrib import admin
from .models import case_table
# Register your models here.

class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_name')

admin.site.register(case_table)