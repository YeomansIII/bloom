from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^play/$', views.play),
    url(r'^signup/$', views.create_user),
    url(r'^login/$', views.login_user),
    url(r'^logout/', views.logout_user),
    url(r'^$', views.index),
]
