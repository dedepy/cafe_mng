from django.urls import path
from .views import (
    OrderListView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    OrderRevenueView
)


urlpatterns = [
    # Список заказов
    path('', OrderListView.as_view(), name='order_list'),

    # Добавление заказа
    path('add/', OrderCreateView.as_view(), name='order_add'),

    # Обновление заказа
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),

    # Удаление заказа
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),

    # Статистика выручки
    path('revenue/', OrderRevenueView.as_view(), name='order_revenue'),
]