from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from api import urls as api_urls
from app import urls as app_urls

urlpatterns = [
                  url(r'^login/$', auth_views.login, name='login'),
                  url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
              ] + api_urls.urlpatterns + app_urls.urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
