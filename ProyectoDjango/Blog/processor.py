from Blog.models import Category, Article

def Get_categorias(request):

    ids_categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)

    categories = Category.objects.filter(id__in=ids_categories_in_use).values_list('id', 'name')

    return{
        'Categoriass': categories,
        'ID': ids_categories_in_use
    }