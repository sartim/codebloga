from django.core.urlresolvers import reverse_lazy
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


class HomeView(generic.ListView):
    template_name = 'blog/my-home.html'
    context_object_name = 'all_posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(generic.DetailView):
        model = Post
        template_name = 'blog/post_detail.html'


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'image', 'code', 'content', 'draft', 'publish']


class PostUpdate(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'image', 'code', 'content', 'draft', 'publish']


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    template_name = "blog/confirm_delete.html"


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



