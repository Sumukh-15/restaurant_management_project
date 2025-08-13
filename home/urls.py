from django.urls import path
from .views import *

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact_us,name='contact_us'),
    path('reservations/',views.reservations,name='reservations'),
]