from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


class HomeView(generic.ListView):
    template_name = 'blog/home.html'
    context_object_name = 'all_posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(generic.DetailView):
        model = Post
        template_name = 'blog/post_detail.html'


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'body', 'code', 'pub_date', 'likes', 'image']


class PostUpdate(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'body', 'code', 'pub_date', 'likes', 'image']


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    template_name = "blog/confirm_delete.html"



