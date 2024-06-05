from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Order

@receiver(post_save, sender=Order)
def notify_client(sender, instance, created, **kwargs):
    if created:
        # Получаем информацию о заказе и пользователе
        order_title = instance.title
        customer_email = instance.customer.email

        # Формируем сообщение
        subject = f"Новый заказ: {order_title}"
        message = f"Уважаемый клиент,\n\nВаш заказ '{order_title}' был успешно создан.\n\nОписание: {instance.description}\n\nСпасибо за использование наших услуг!"
        from_email = settings.DEFAULT_FROM_EMAIL

        # Отправляем сообщение
        send_mail(subject, message, from_email, [customer_email])