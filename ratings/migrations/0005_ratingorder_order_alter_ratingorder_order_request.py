# Generated by Django 5.0.3 on 2024-04-24 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0008_remove_order_order_taken_remove_order_order_taken_at'),
        ('ratings', '0004_ratingorder_user_alter_ratingorder_order_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingorder',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_rating', to='freelance.order', verbose_name='Заказ'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ratingorder',
            name='order_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.orderrequest', verbose_name='Заявка на заказ'),
        ),
    ]
