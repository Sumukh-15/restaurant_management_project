from django.shortcuts import render
from products.models import Menu

# Create your views here.
def homepage(request):
    menu_items = Menu.objects.all()
    context={
        'menu_items':menu_items,
        'restaurant_name':settings.RESTAURANT_NAME
        'phone_number':settings.RESTAURANT_PHONE
    }
    return render(request,'home/homepage.html',{'menu_items':menu_items})

def contact_us(request):
    contact_info = {
        'phone': '+91-9876543210'
        'email': 'info@restaurant.com'
        'address': '123 Food Street, Kochi, Kerala'
    }
    return render(request,'contact_us.html',{'contact':contact_info})
