from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from Blog.models import Category, Article
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="Loguearse")
def Articulos_En_Lista(request):

    # Sacar los artículos
    article = Article.objects.all()

    # Paginar los artículos
    paginar = Paginator(article, 10)

    # Recoger número página
    page = request.GET.get('page')
    page_articles = paginar.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articulicos': page_articles
    })

@login_required(login_url="Loguearse")
def Categorias(request, category_id):

    categoria = get_object_or_404(Category, id=category_id)
    mostrar_articulo_por_categoria = Article.objects.filter(categories=category_id)

    return render(request, 'categories/category.html', {
        'categoriaA': categoria,
        'articulicos': mostrar_articulo_por_categoria
    })

@login_required(login_url="Loguearse")
def Articulo_En_Cada_Una_De_Las_Paginas(request, article_id):

    Articulo = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html', {
        'ARTICULOO': Articulo
    })