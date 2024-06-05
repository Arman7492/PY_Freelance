# Generated by Django 5.0.3 on 2024-03-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0002_customer_rating_executor_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='executor',
            name='rating',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rating',
            field=models.FloatField(default=0.0, verbose_name='Рейтинг'),
        ),
    ]