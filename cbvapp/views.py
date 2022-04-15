from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from .models import Post


class Ex2View(TemplateView):
    template_name = 'ex2.html'

    def get_context_data(self, **kwargs):
        context = super(Ex2View, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(id=1)
        context['data'] = 'This is Template view'
        return context


class PostPreLoaderView(RedirectView):
    pattern_name = 'single'

    def get_redirect_url(self, *args, **kwargs):
        post = Post.objects.filter(pk=self.kwargs.get('pk'))
        post.update(view=F('view')+1)
        return super().get_redirect_url(*args, **kwargs)


class SinglePageView(TemplateView):
    template_name = 'ex3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context
