from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    list_filter = ('title', 'description', 'image')
    search_fields = ('title', 'description', 'image')

admin.site.register(Service, ServiceAdmin)