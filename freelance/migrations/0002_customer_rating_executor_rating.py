# Generated by Django 5.0.3 on 2024-03-31 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='rating',
            field=models.FloatField(default=0.0, verbose_name='Рейтинг'),
        ),
        migrations.AddField(
            model_name='executor',
            name='rating',
            field=models.FloatField(default=0.0, verbose_name='Рейтинг'),
        ),
    ]