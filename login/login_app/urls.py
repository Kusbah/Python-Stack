
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('success',views.register,name='success'),
    path('login',views.login),
    path('dashboard', views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout')
]
