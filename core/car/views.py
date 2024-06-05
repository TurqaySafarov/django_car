from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Owner
from .forms import CarForm, OwnerForm

def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})

def owner_detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'owner_detail.html', {'owner': owner})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

def add_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OwnerForm()
    return render(request, 'add_owner.html', {'form': form})
