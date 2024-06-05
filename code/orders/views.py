from django.core.checks import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.utils import timezone
from datetime import timedelta
from .models import Order
from .forms import OrderForm
from customers.models import Customer
from executers.models import Executor


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/create_order.html"
    success_url = "/orders/"

    def form_valid(self, form):
        form.instance.customer = Customer.objects.get(user=self.request.user)

        return super().form_valid(form)


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"


class OrderTakeView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = []
    template_name = "orders/order_take.html"
    success_url = "/orders/"

    def form_valid(self, form):
        order = form.save(commit=False)
        if hasattr(self.request.user, "executor_profile") and not order.is_taken:
            order.executor = Executor.objects.get(user=self.request.user)
            order.deadline = timezone.now() + timedelta(days=10)

            order.is_taken = True
            order.save()

        return super().form_valid(form)

class OrderEditView(LoginRequiredMixin, UpdateView):
    template_name = "orders/create_order.html"
    form_class = OrderForm
    model = Order
    success_url = "/orders/"

    def form_valid(self, form):
        form.instance.customer = Customer.objects.get(user=self.request.user)
        return super().form_valid(form)


class OrderDelete(DeleteView):
    model = Order
    success_url = "/orders/"

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(OrderDelete, self).form_valid(form)