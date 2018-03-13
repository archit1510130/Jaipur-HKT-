from django.conf.urls import url,include
from . import views
from django.views.generic.base import TemplateView

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [

    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url('', views.index, name='index'),

 ]
