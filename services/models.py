from django.db import models

<<<<<<< HEAD
# Create your models here.
class Service(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250, blank=False, null=False)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="services/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
=======
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название услуги')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(null=True, verbose_name='Изображение', upload_to="services/")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
>>>>>>> ffce688842ec1fa75373b03dbab3af6db23f1b1a
