from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import CommentForm

# Create your views here.


def index(request):
    """ The home page for Pizzeria """
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')

    context = {'pizzas': pizzas}


    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    topping = pizza.topping_set.order_by('name')
    comment = pizza.comment_set.order_by('date_added')

    context = {'pizza': pizza, 'topping': topping, 'comment': comment}

    return render(request, 'pizzas/pizza.html', context)

def comments(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        comment = CommentForm()
    else:
        comment = CommentForm(data=request.POST)

        if comment.is_valid():
            comments = comment.save()

            return redirect('pizzas:pizzas')
    context = {'comment':comment, 'pizza': pizza}
    return render(request, 'pizzas/comments.html', context)
        
