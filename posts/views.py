from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from . models import Post, Category
from . forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
#def index(request):
 #   return render(request, "base/index.html", {})

class HomeView(ListView):
    model = Post
    template_name = 'base/index.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cate_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cate_menu"] = cate_menu
        return context

def CategoryView(request, cate):
    category_posts = Post.objects.filter(category=cate)
    return render(request, 'base/category.html', {"cate": cate.title(), 'category_posts': category_posts})

class ArticalDetailView(DetailView):
    model = Post
    template_name = 'base/detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'base/add_post.html'
    #fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'base/add_categories.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'base/delete.html'
    success_url = reverse_lazy('home')