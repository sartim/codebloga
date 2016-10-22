from django.core.urlresolvers import reverse_lazy
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from .models import Post


class HomeView(generic.ListView):
    template_name = 'blog/my-home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all()


# Create your views here.
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def register(request):
    """Renders the register page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'blog/register.html',
        context_instance = RequestContext(request,
        {
            'title':'Register',
            'message':'This is the register page.',
            'year': datetime.now().year,
        })
    )


def register_user(request):
    """Renders the register_user page."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('blog/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()
    print (args)
    return render('blog/register.html', args)


def register_success(request):
    """Renders the register_success page."""
    return render('blog/register_success.html')


def login(request):
    """Renders the login page."""
    c = {}
    c.update(csrf(request))
    return render('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('blog/loggedin')
    else:
        return HttpResponseRedirect('blog/invalid')


def loggedin(request):
    """Renders the loggedin page."""
    return render('blog/loggedin.html',
                    {'full_name': request.user.username})


def invalid_login(request):
    """Renders the invalid_login page."""
    return render('blog/invalid_login.html')


def logout(request):
    """Renders the logout page."""
    auth.logout(request)
    return render('blog/logout.html')



