from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.


def index(request):
    """ The home page for Pizzeria """
    return render(request, 'pizzas/index.html')

def zas(request):
    pizza = Pizza.objects.order_by('name')
    #entries = topic.entry_set.order_by('-date_added')

    context = {'pizza': pizza}


    return render(request, 'pizzas/zas.html', context)

def za(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    topping = Topping.entry_set.order_by('name')
    context = {'pizza': pizza, 'topping': topping}

    return render(request, 'pizzas/za.html', context)
