from django.conf.urls import url
from django.contrib import admin
from app import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/', views.add, name='add'),
    url(r'^show/(?P<bikeid>[0-9]+)$', views.show, name='show'),
    url(r'^$', views.index, name='index')
]
