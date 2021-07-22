from django.shortcuts import render, redirect
from .models import Category, Dish, About
import datetime
from .forms import ReservationsForm, MessageForm

# Create your views here.


def main_view(request):

    if request.method == 'POST':
        form = ReservationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    time = datetime.datetime.now()
    categories = Category.objects.filter(is_visible=True).order_by('-cat_order')
    dish = Dish.objects.filter(is_visible=True).filter(is_special=False).order_by('-dish_order')
    dishes_special = Dish.objects.filter(is_special=True)
    about = About.objects.last()
    form = ReservationsForm()
    form_1 = MessageForm()
    return render(request, 'index.html', context={'categories': categories,
                                                  'dishes': dish,
                                                  'dishes_special': dishes_special,
                                                  'about': about,
                                                  'cur_time': time,
                                                  'form_book': form,
                                                  'form_1': form_1})



