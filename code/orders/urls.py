from django.urls import path
from .views import OrderListView, OrderCreateView, OrderDetailView, OrderTakeView, OrderEditView

app_name = "orders"

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('take/<int:pk>/', OrderTakeView.as_view(), name='order_take'),
    path("orders/edit/<int:pk>", OrderEditView.as_view(), name="order_edit"),
]
