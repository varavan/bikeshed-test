"""bikeshed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app import views as app_views
from api import views as api_views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/', app_views.add, name='add'),
    url(r'^show/(?P<bikeid>[0-9]+)$', app_views.show, name='show'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', app_views.index, name='index'),

#     api calls
    url(r'^api/bike/add', api_views.add, name='api_add'),
    url(r'^api/bikes-sorted/(?P<sort>(model|brand|price)\b)/(?P<order>(asc|desc)\b)$', api_views.list_sorted, name='api_list_sorted'),
    url(r'^api/bikes', api_views.list, name='api_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)