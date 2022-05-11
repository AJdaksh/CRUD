"""projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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


admin.site.site_header = "Careers360"
admin.site.site_title = "Careers Portal"
admin.site.index_title = "Welcome to Careers360 Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('contact',include('home.urls')),
    path('about',include('home.urls')),
    path('delete/<int:id>',include('home.urls')),
    path('<int:id>',include('home.urls')),
    path('filte',include('home.urls')),
    path('login',include('home.urls')),
    path('signup',include('home.urls')),
    path('profile',include('home.urls')),
]

   # path('about/community',include('home.urls')),