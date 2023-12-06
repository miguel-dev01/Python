from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.Articulos_En_Lista, name="Articulos"),
    path('categorias/<int:category_id>', views.Categorias, name="Categorias"),
    path('articulo/<int:article_id>', views.Articulo_En_Cada_Una_De_Las_Paginas, name="Articulo-En-Cada-Pagina")
]
