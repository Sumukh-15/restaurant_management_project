from django.shortcuts import render
from products.models import Menu

# Create your views here.
def homepage(request):
    menu_items = Menu.objects.all()
    context={
        'menu_items':menu_items,
        'restaurant_name':settings.RESTAURANT_NAME
    }
    return render(request,'home/homepage.html',{'menu_items':menu_items})
