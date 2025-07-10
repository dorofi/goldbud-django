from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('zamow-wycene/', views.order_view, name='order_form'),
    path('uslugi/', views.services, name='services'),
    path('otzyvy/', views.testimonials, name='testimonials'),
    path('kontakty/', views.contact, name='contact'),
    path('test/', views.test_view),
]