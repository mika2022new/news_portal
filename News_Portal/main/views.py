from django.urls import reverse_lazy

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .filters import PostFilter
from .forms import PostForm
from .models import Post


from datetime import datetime
from pprint import pprint

from django.contrib.auth.mixins import LoginRequiredMixin


class NewsList(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'news.html'
    context_object_name = 'news'

    paginate_by = 7


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset

        pprint(context)
        return context

class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class NewsCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news._type = 'NE'
        return super().form_valid(form)


class ArticleCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article._type = 'AR'
        return super().form_valid(form)


class NewsUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'new_delete.html'
    success_url = reverse_lazy('post_list')


class SearchList(ListView):
    model = Post
    template_name = 'search_page.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context