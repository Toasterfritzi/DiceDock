from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='characters/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('create/', views.create_character, name='create_character'),
    path('character/<int:pk>/', views.character_detail, name='character_detail'),
    path('character/<int:pk>/levelup/', views.character_levelup, name='character_levelup'),
    path('character/<int:pk>/update_stat/', views.update_character_stat, name='update_character_stat'),
    path('character/<int:pk>/update_coin/', views.update_character_coin, name='update_character_coin'),
    path('character/<int:pk>/add_weapon/', views.add_character_weapon, name='add_character_weapon'),
    path('build/', views.character_builder, name='character_builder'),
    path('build/submit/', views.character_builder_submit, name='character_builder_submit'),
]
