from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('books',views.books,name='books'),
    path('add',views.addBook,name="addBook"),
    path('books/<int:id>',views.view_book,name='view_book'),
    path('books/<int:id>/update', views.update_book, name='update_book'),
    path('books/<int:id>/delete', views.delete_book, name='delete_book'),
    path('books/<int:id>',views.view_book_user,name='view_book_user'),
    path('books/<int:id>/favorite', views.favorite_book, name='favorite_book'),
path('books/<int:id>/unfavorite', views.unfavorite_book, name='unfavorite_book'),
]
