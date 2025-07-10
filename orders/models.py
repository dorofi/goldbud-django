from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField("Imię i nazwisko", max_length=100)
    address = models.CharField("Adres obiektu", max_length=200)
    phone = models.CharField("Telefon", max_length=30)
    details = models.TextField("Opis pracy")
    created_at = models.DateTimeField(auto_now_add=True)

    # Для загрузки нескольких фото — отдельная модель
    def __str__(self):
        return f"{self.name} ({self.phone}) — {self.created_at:%Y-%m-%d}"  

class OrderPhoto(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField("Zdjęcie", upload_to='order_photos/')

    def __str__(self):
        return f"Фото для заявки {self.order_id}"
