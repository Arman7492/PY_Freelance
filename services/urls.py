from django.urls import path
from .views import (
    ServiceListView,
    ServiceDetailView,
    ServiceUpdateView,
    ServiceCreateView,
)

app_name = 'services'

urlpatterns = [
    path("", ServiceListView.as_view(), name="services_list"),
    path("<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),
    path("update/<int:pk>", ServiceUpdateView.as_view(), name="service_update"),
    path("create/", ServiceCreateView.as_view(), name="service_create"),
    
]