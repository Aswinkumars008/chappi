from django.shortcuts import render,redirect
from .models import Contact,Product


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        message = Contact(name=name, email=email, content=content)
        message.save()
        return redirect('index')  # Redirect back to the index page after saving the message

    return render(request, 'index.html')


def snacks(request):
    snacks = Product.objects.filter(category='snack')
    return render(request, 'snacks.html', {'snacks': snacks})

def hotdrinks(request):
    hot_drinks = Product.objects.filter(category='hot_drink')
    return render(request, 'hotdrinks.html', {'hot_drinks': hot_drinks})

def cooldrinks(request):
    cold_drinks = Product.objects.filter(category='cold_drink')
    return render(request, 'cooldrinks.html', {'cold_drinks': cold_drinks})