from django.urls import path
from . import views
urlpatterns = [
    path('show/new',views.index,name='create'),
    path('show/<int:id>/', views.show_detail, name='show_detail'),
    path('show',views.shows,name='show'),
    path('show/<int:id>/delete/', views.delete_show, name='delete_show'),
    path('show/<int:id>/edit/', views.edit_show, name='edit_show')

]
