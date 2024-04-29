"""
URL configuration for rainbow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rainbowpictures.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="Home"),
    path('portfolio/',Portfolio,name="Portfolio"),
    path('contact/',Contact,name="Contact"),
    path('clients/',Clients,name="Clients"),
    path('about/',About,name="About"),
    path('blog/',Blog,name="Blog"),
    path('services/',Service,name="Services"),
    path('candid/',Candid,name="Candid"),
    path('marketing/',Marketing,name="Marketing"),
    path('formsubmit/',Formsubmit,name="Formsubmit"),
    path('sendemail/',send_email,name="sendemail"),
]
