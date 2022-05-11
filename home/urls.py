from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact',views.index,name='home'),
    path('',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('<int:id>',views.update,name='update'),
    path('filte_n',views.filter_n,name='filte_n'),
    path('filte_e',views.filter_e,name='filte_e'),
    path('filte_m',views.filter_m,name='filte_m'),
    path('filte_i',views.filter_i,name='filte_i'),
    path('login',views.login,name='login'),
    path('signup',views.sign_up,name='signup'),
    path('profile',views.profile,name='profile'),
]
    #path('about/community',views.community,name='community'),