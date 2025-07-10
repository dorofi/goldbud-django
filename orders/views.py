from django.shortcuts import render, redirect
from django.conf import settings
from pathlib import Path
from .forms import OrderForm
from .models import Order, OrderPhoto
import requests

def index(request):
    return render(request, "orders/index.html")

def galeria(request):
    # The path should point to 'static/gallery/' as recommended previously.
    # Using pathlib is more robust for handling file paths.
    gallery_dir = Path(settings.BASE_DIR) / "static" / "gallery"
    images = []
    # Check if the directory exists to avoid errors.
    if gallery_dir.is_dir():
        # Find all image files.
        for f in gallery_dir.iterdir():
            if f.is_file() and f.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp", ".gif"]:
                # Create a URL that the template can use.
                # The previous f-string was broken due to a copy-paste error.
                images.append({"url": f"{settings.STATIC_URL}gallery/{f.name}"})
    context = {"images": images}
    return render(request, "orders/galeria.html", context)

def order_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            # Сохраняем фото
            for f in request.FILES.getlist("photos"):
                OrderPhoto.objects.create(order=order, image=f)
            # Отправляем в Telegram
            send_telegram(order, request.FILES.getlist("photos"))
            return render(request, "orders/order_success.html", {"order": order})
    else:
        form = OrderForm()
    return render(request, "orders/order_form.html", {"form": form})

def send_telegram(order, photos):
    token = getattr(settings, "TELEGRAM_TOKEN", None)
    chat_id = getattr(settings, "TELEGRAM_CHAT_ID", None)
    if not token or not chat_id:
        return
    text = (
        f"<b>Nowe zgłoszenie z formularza:</b>\n"
        f"<b>Imię i nazwisko:</b> {order.name}\n"
        f"<b>Adres obiektu:</b> {order.address}\n"
        f"<b>Telefon:</b> {order.phone}\n"
        f"<b>Opis:</b> {order.details}"
    )
    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    )
    # Отправка фото
    for photo in photos:
        files = {"photo": photo}
        data = {"chat_id": chat_id}
        requests.post(f"https://api.telegram.org/bot{token}/sendPhoto", data=data, files=files)

# --- Страницы: услуги, отзывы, контакты ---
def services(request):
    return render(request, "orders/services.html")

def testimonials(request):
    return render(request, "orders/testimonials.html")

def contact(request):
    return render(request, "orders/contact.html")

def test_view(request):
    return render(request, 'orders/test.html')
