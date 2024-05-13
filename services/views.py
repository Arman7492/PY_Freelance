from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ServiceForm
from .models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'services/services_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    from_class = ServiceForm

class ServiceCreateView(CreateView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    success_url = reverse_lazy('services:services_list')
    form_class = ServiceForm

class ServiceUpdateView(UpdateView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    success_url = reverse_lazy('services:services_list')
    form_class = ServiceForm
