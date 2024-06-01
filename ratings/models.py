from django.db import models
<<<<<<< HEAD
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Rating(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    rated_by = models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='given_ratings')
    rating = models.PositiveIntegerField(verbose_name='Рейтинг', default=0)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    def __str__(self):
        return f"{self.rating} by {self.rated_by.username} to {self.user.username}"
    

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
=======
from freelance.models import OrderRequest


class RatingOrder(models.Model):
    order = models.ForeignKey(
        to="freelance.Order",
        verbose_name="Заказ",
        on_delete=models.CASCADE,
        related_name="order_rating",
    )
    testimonial = models.TextField(verbose_name="Отзыв", blank=True, null=True)

    user = models.ForeignKey(
        to="freelance.UserProfile",
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="user_rating",
        null=True,
        blank=True,
    )

    order_rating = models.FloatField(verbose_name="Рейтинг", blank=True, null=True)

    def __str__(self):
        return (
            self.order.customer.profile.user.username
            or self.order.executor.profile.user.username
        )

    class Meta:
        unique_together = ("order", "user")
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
>>>>>>> ffce688842ec1fa75373b03dbab3af6db23f1b1a
