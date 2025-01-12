from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Page

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'page/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = 'page/page_detail.html'
    context_object_name = 'page'