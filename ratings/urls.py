<<<<<<< HEAD
from django.contrib import admin
from django.urls import path

app_name = 'ratings'

urlpatterns = [
=======
from django.urls import path

from ratings.views import RatingListView, RatingUpdateView

app_name = "ratings"

urlpatterns = [
    path("all/", RatingListView.as_view(), name="rating_list"),
    path("update/<int:order>/", RatingUpdateView.as_view(), name="rating_update"),
>>>>>>> ffce688842ec1fa75373b03dbab3af6db23f1b1a
]