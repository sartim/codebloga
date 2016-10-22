"""codebloga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from datetime import datetime
from django.conf.urls import url, include
from blog.forms import BootstrapAuthenticationForm
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from blog.views import HomeView, register, register_success, post_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^$', post_list, name='home'),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^register', register, name='register'),
    url(r'^register_success$', register_success, name='register_success'),
    url(r'^login/$', login,
        {
            'template_name': 'blog/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
                {
                    'title': 'Log in',
                    'year': datetime.now().year,
                }
        },
        name='login'),
    url(r'^logout$', logout,
        {
            'next_page': '/',
        },
        name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
