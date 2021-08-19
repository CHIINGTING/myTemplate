"""myTemplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
#    path('<int:tvno>/', views.yt, name='tv-url')
    path('<int:tvno>/', views.index, name='tv-url'),
    path('engtv/', views.engtv),
    path('engtv/<int:tvno>', views.engtv, name='engtv-url'),
    path('carlist/', views.carlist),
    path('carlist/<int:maker>/', views.carlist, name='carlist-url'),
    path('carprice/', views.carprice),
    path('carprice/<int:maker>/', views.carprice, name='carprice-url'),
]
