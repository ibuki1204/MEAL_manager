# mealtracker/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meals/', include('meals.urls')),  # mealsアプリのURLを読み込む
]



