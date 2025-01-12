from .models import Page

def page_list(request):
    published_pages = Page.objects.filter(status=Page.Status.PUBLISHED)
    return {
        'page_list': published_pages
    }