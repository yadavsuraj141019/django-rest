"""
URL configuration for CarDekho project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from CarDekho_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/list', car_list_view, name="car_list_view"),
    path('car/list/<int:id>/', car_detail_view, name="car_detail_view"),
    path('showroom/',Showroom_View.as_view(),name="Showroom_View"),
    path('showroom/<int:id>/',Showroom_Details.as_view(),name="Showroom_Details"),
]
