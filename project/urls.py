"""project URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #The Main Views
    url(r'home_view/$', 'main.views.home_view'),
    url(r'about_view/$', 'main.views.about_view'),
    url(r'client_view/$', 'main.views.client_view'),
    url(r'contact_view/$', 'main.views.contact_view'),

    #The Client Views
    url(r'thrive_client/$', 'main.views.thrive_client'),
    url(r'title_client/$', 'main.views.title_client'),
    url(r'ring_client/$', 'main.views.ring_client'),
    url(r'nectar_client/$', 'main.views.nectar_client'),

    #Map view
    url(r'map/$', 'main.views.map_view')
]
