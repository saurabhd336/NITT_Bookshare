from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^signin/', views.signin),
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.test),
    url(r'^logout/', views.logout_view),
]
