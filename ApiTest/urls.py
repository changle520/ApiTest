"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from MyApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),url(r'^welcome/$',welcome),url('^caselist/$',case_list),url('^home/$',home),url(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", child),url(r'^login/$',login),
    url(r'^login_action/$',login_action),url(r'^register_action/$',register_action),url(r'^accounts/login/$',login),url(r'^logout/$',logout),url(r'^pei/$',pei),url(r'^help/$',api_help),
    url(r'^project_list/$',project_list),url(r"^delete_project/$",delete_project),url(r"^add_project/$",add_project),url(r"^apis/(?P<id>.*)/$",open_apis),url(r"^cases/(?P<id>.*)/$",open_cases),
    url(r"^project_set/(?P<id>.*)/$",open_project_set),url(r'^save_project_set/(?P<id>.*)/$',save_project_set),url(r"^save_bz/$",save_bz),url(r"^get_bz/$",get_bz),url(r'^Api_save/$',Api_save),
    url(r"^get_api_data/$",get_api_data),url(r"^Api_send/$",Api_send),url(r'^copy_api/$',copy_api),url(r'^error_request/$',error_request)
]

# urlpatterns=[url(r'^admin/',admin.site.urls),url(r'^MyApp/',include('MyApp.urls'))]