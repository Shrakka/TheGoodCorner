from django.conf.urls import url
from . import views
import os.path


app_name = 'goodcorner'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^announce/(?P<pk>[0-9]+)$', views.AnnounceView.as_view(), name='announce'),
    url(r'^create$', views.CreateAnnounceView.as_view(), name='create'),
    url(r'^contact/(?P<pk>[0-9]+)$', views.contact, name='contact'),
    url(r'^edit/(?P<hashurl>[0-9A-Fa-f-]+)$', views.edit, name='edit'),
    url(r'^delete/(?P<hashurl>[0-9A-Fa-f-]+)$', views.delete, name='delete'),
]
