from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout,name='logout'),
    path('createproject',views.Project_page,name='createproject'),
    path('createproject/', views.createProject, name='create_project'),
    path('project/<int:project_id>/details/', views.projectDetails, name='projectDetails'),
    path('editproject/<int:project_id>', views.editProject, name='editproject'),
    path('project/<int:project_id>/delete/', views.deleteProject, name='deleteproject'),
    path('project/<int:project_id>/join/', views.joinProject, name='joinproject'),
    path('project/<int:project_id>/separate/', views.separateProject, name='separateproject'),
]