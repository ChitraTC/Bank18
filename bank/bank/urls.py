"""
URL configuration for bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name="home"),
    re_path(r'^accounts/', include("accounts.urls")),
    re_path(r'^profile/', include("profiles.urls")),
    re_path(r'^admins/', include("admins.urls"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Change Site Title, Index Title and Site Title
admin.site.site_header = "Bank 4 You Administration"
admin.site.site_title = "B4U Administration"
admin.site.index_title = "Welcome to B4U Admin Panel"

