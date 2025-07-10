from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    photos = forms.FileField(
        label="Załącz zdjęcia (opcjonalnie)",
        required=False
    )

    class Meta:
        model = Order
        fields = ["name", "address", "details", "phone"]
        widgets = {
            "details": forms.Textarea(attrs={"rows": 4}),
        }