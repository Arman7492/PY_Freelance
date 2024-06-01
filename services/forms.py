<<<<<<< HEAD
from django import forms
from .models import Service


class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["title", "description", "image"]
=======
# from django.forms import ModelForm
from django.forms import ModelForm
from .models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'image']

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["title"].widget.attrs.update(
        {"class": "form-control","placeholder": "Название"}
    )
    self.fields["description"].widget.attrs.update(
        {"class": "form-control", "placeholder": "Описание"}
    )
    self.fields["image"].widget.attrs.update(
        {"class": "form-control align-items-center", "placeholder": "Изображение" }
    )
>>>>>>> ffce688842ec1fa75373b03dbab3af6db23f1b1a
