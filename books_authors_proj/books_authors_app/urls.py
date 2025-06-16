from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('authors/',views.author),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail')
]