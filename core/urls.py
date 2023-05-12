"""
URL configuration for core project.

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
from django.urls import path
from core.settings import *

from home.views import *

from vege.views import *


urlpatterns = [

    path('', home, name = "home"),

    path('receipes/' , receipes , name = "receipes"),
    path('delete_receipes/<id>/' , delete_receipes , name = "delete_receipes"),
    path('contact/' , contact , name = "contact"),
    
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns += STATIC_ROOT(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()

