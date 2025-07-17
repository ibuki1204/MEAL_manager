"""
URL configuration for mealtracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from meals import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('meals/', include('meals.urls')),
    path('add/', views.add_meal, name='add_meal'),  # ← これで OK
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

urlpatterns = [
    path('add/', views.add_meal, name='add_meal'),
    # 他のビューも追加
]
