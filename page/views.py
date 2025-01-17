from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Page, HomeBlock

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'page/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['blocks'] = HomeBlock.objects.all().order_by('order')
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = 'page/page_detail.html'
    context_object_name = 'page'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_images'] = self.object.page_header_images.all()
        context['slider_blocks'] = self.object.slider_blocks.all()
        context['banner_blocks'] = self.object.banner_blocks.all()
        return context