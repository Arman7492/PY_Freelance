<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from .views import CreateServiceView, DeleteServiceView, ServiceListView
=======
from django.urls import path
from .views import (
    ServiceListView,
    ServiceDetailView,
    ServiceUpdateView,
    ServiceCreateView,
)
>>>>>>> ffce688842ec1fa75373b03dbab3af6db23f1b1a

app_name = 'services'

urlpatterns = [
<<<<<<< HEAD
    path("", ServiceListView.as_view(), name="service_list"),
    path("create/", CreateServiceView.as_view(), name="create"),
    path("delete/<int:pk>/", DeleteServiceView.as_view(), name="delete"),
=======
    path("", ServiceListView.as_view(), name="services_list"),
    path("<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),
    path("update/<int:pk>", ServiceUpdateView.as_view(), name="service_update"),
    path("create/", ServiceCreateView.as_view(), name="service_create"),
    
>>>>>>> ffce688842ec1fa75373b03dbab3af6db23f1b1a
]