from django.shortcuts import render
from itertools import chain

from django.utils.safestring import mark_safe
from django.views.generic import TemplateView, DetailView, ListView
from markdown import markdown



from .models import *




class HomePageView(ListView):
    template_name = 'mvpcode/index.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        alrticles = Article.objects.filter(is_published=True)[:6]
        all_content = list(chain(alrticles))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alrticles'] = [content for content in context['all_content'] if isinstance(content, Article)]
        return context



class ArticlesView(ListView):
    template_name = 'mvpcode/articles.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        alrticles = Article.objects.filter(is_published=True).order_by('-time_create')
        all_content = list(chain(alrticles))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alrticles'] = [content for content in context['all_content'] if isinstance(content, Article)]
        return context



class ArticlesDetail(DetailView):
    model = Article
    template_name = 'mvpcode/articledetail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context['article']
        # Преобразуйте текст статьи из Markdown в HTML
        html_text = mark_safe(markdown(article.text))
        context['html_text'] = html_text
        return context




class CourcesPageView(TemplateView):
    template_name = 'mvpcode/cources.html'



class ContactPageView(TemplateView):
    template_name = 'mvpcode/contacts.html'
