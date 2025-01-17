from .models import Page

def pages_processor(request):
    """
    Context processor que retorna todas las páginas publicadas
    para ser usadas en el navbar
    """
    published_pages = Page.objects.filter(status=Page.Status.PUBLISHED).order_by('title')
    return {
        'nav_pages': published_pages
    }