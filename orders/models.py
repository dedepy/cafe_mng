from django.core.exceptions import ValidationError
from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('в ожидании', 'В ожидании'),
        ('готово', 'Готово'),
        ('оплачено', 'Оплачено')
    ]

    table_number = models.PositiveIntegerField(
        help_text="Номер стола (только положительные числа)"
    )
    items = models.TextField(
        help_text="Список товаров в формате 'название:цена, название:цена'"
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        help_text="Общая стоимость заказа"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='в ожидании',
        help_text="Текущий статус заказа"
    )

    def __str__(self):
        """Строковое представление заказа."""
        return f"Заказ {self.id} стола №{self.table_number}"

    def clean(self):
        super().clean()
        if self.table_number <= 0:
            raise ValidationError({'table_number': 'Номер стола должен быть положительным'})

        # Проверка формата списка товаров
        try:
            self.calculate_total_price()
        except ValueError:
            raise ValidationError({'items': 'Неверный формат списка товаров. Используйте "название:цена, название:цена"'})

    def save(self, *args, **kwargs):

        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)

    def calculate_total_price(self):

        total_price = 0
        items = self.items.split(',')
        for item in items:
            if ':' not in item:
                raise ValueError("Неверный формат элемента товара")
            name, price = item.strip().split(':')
            total_price += float(price.strip())
        return round(total_price, 2)