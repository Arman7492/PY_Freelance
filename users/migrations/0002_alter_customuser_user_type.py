# Generated by Django 5.0.6 on 2024-05-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'customer'), (2, 'executor')], default=1, verbose_name='Тип пользователя'),
        ),
    ]
