from django.db.models import Sum, Q
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Order
from .forms import OrderForm

# Список заказов с поиском
class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '').lower()
        if search_query:
            queryset = queryset.filter(
                Q(table_number__icontains=search_query) | Q(status__icontains=search_query)
            )
        return queryset


# Добавление заказа
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('order_list')


# Обновление заказа
class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('order_list')


# Удаление заказа
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'orders/order_delete.html'
    success_url = reverse_lazy('order_list')


# Статистика выручки
class OrderRevenueView(TemplateView):
    template_name = 'orders/order_revenue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_revenue = Order.objects.filter(status='оплачено').aggregate(Sum('total_price'))['total_price__sum'] or 0
        context['total_revenue'] = total_revenue
        return context