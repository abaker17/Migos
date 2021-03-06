"""ribbit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from ribbit_app.views import index, login_view, logout_view, signup, public, submit, users, follow

urlpatterns = [
    url(r'^$', index, name='root'), # root
    url(r'^login$', login_view, name='login'), # login
    url(r'^logout$', logout_view, name='logout'), # logout
    url(r'^signup$', signup, name='signup'), # signup
    url(r'^submit$', submit, name='submit'), # submit new ribbit
    url(r'^ribbits$', public, name='ribbits'), # public ribbits
    url(r'^users/$', users, name='users'),
    url(r'^users/(?P<username>\w{0,30})/$', users, name='users'),
    url(r'^follow$', follow, name='follow'),

]
