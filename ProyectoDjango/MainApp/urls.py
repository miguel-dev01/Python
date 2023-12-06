from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="Index"),
    path('inicio/', views.Index, name="Inicio"),
    path('registro/', views.Register_Page, name="Registrar"),
    path('login/', views.Login_Page, name="Loguear"),
    path('logout', views.Logout_User, name="Desloguearse")
]
