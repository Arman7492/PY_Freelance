from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # self.fields['deadline'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        
        

    class Meta:
        model = Order
        fields = ['title', 'description', 'service', 'price']


    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
        return order

    def delete(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.delete()
        return order
