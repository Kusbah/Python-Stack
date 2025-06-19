from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register',views.registration,name='register'),
    path('post_message', views.post_message, name="post_message"),
    path('well', views.message_wall, name="well"),
]