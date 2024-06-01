from django.contrib import admin
from .models import Service

<<<<<<< HEAD
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

admin.site.register(Service, ServicesAdmin)
=======
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    list_filter = ('title', 'description', 'image')
    search_fields = ('title', 'description', 'image')

admin.site.register(Service, ServiceAdmin)
>>>>>>> ffce688842ec1fa75373b03dbab3af6db23f1b1a
