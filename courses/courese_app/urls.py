from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('<int:id>/confirm/',views.confirm,name='confirm'),
    path('<int:id>/delete/',views.remove,name='remove'),
]
