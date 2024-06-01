from django.contrib import admin
<<<<<<< HEAD

from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'rated_by', 'rating']

admin.site.register(Rating, RatingAdmin)
=======
from ratings.models import RatingOrder


@admin.register(RatingOrder)
class RatingOrderAdmin(admin.ModelAdmin):
    list_display = ("order", "user", "testimonial") 
    


# Register your models here.
>>>>>>> ffce688842ec1fa75373b03dbab3af6db23f1b1a
