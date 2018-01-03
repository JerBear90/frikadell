"""frikadell URL Configuration

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
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from public import views as public_views, urls as public_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^robots\.txt', public_views.robots, name='robots'),
    url(r'^sitemap\.xml', public_views.sitemap, name='sitemap-xml'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', public_views.index),
]

urlpatterns += i18n_patterns(
    url(r'^', include(public_urls.public_site_patterns, namespace=public_urls.app_name))
)
