from django.shortcuts import render

from orders.models import Order
from services.models import Service
from executers.models import Executor
from customers.models import Customer
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainpage/mainpage.html"
    context_object_name = "orders"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        services = Service.objects.all()
        executors = Executor.objects.filter()
        customers = Customer.objects.filter()
        context = {
            'orders': orders,
            'services': services,
            'executors': executors,
            'customers': customers,
        }
        return context
