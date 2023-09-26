from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from django.core.paginator import Paginator
from .models import Post
from .filters import PostFilter

class PostList(ListView):
    model = Post
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 10

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
       return context

class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'

class Posts(View):
    def get(self, request):

        posts = Post.objects.order_by('-dateCreation')
        p = Paginator(posts, 1)
        posts = p.get_page(request.GET.get('page', 1))

        data = {
        'posts': posts,
        }

        return render(request, 'news/posts.html', data)

class SearchView(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'search'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

