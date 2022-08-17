from importlib.resources import path
from django.urls import path
from FirstApp import views

appName = 'FirstApp'

urlpatterns = [
    path('', views.FirstAppView, name='FirstApp'),
    path('form/', views.Register, name='form'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
]