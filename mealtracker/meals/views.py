from django.shortcuts import render, redirect
from .forms import MealForm
from .models import Meal
from django.contrib.auth.decorators import login_required

@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('meal_list')
    else:
        form = MealForm()
    return render(request, 'meals/add_meal.html', {'form': form})

# meals/views.py

from django.http import HttpResponse

def add_meal(request):
    return HttpResponse("これは食事登録ページです")

