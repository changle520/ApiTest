from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from MyApp.views import *

#
# urlpatterns = [
#     path('admin/', admin.site.urls),url(r'^welcome/',welcome),url('^caselist/',case_list),url('^home/',home),url(r"^child/(?P<eid>.+)/(?P<oid>.*)/", child),url(r'^login/',login),
#     url(r'^login_action/',login_action),url(r'^register_action/',register_action),url(r'^accounts/login/',login),url(r'^logout/',logout),url(r'^pei/',pei),url(r'^help/',api_help),
#     url(r'^project_list/',project_list),url(r"^delete_project/",delete_project),url(r"^add_project/",add_project),url(r"^apis/(?P<id>.*)/",open_apis),url(r"^cases/(?P<id>.*)/",open_cases),
#     url(r"^project_set/(?P<id>.*)/",open_project_set),url(r'^save_project_set/(?P<id>.*)/',save_project_set),url(r"^save_bz/",save_bz),url(r"^get_bz/",get_bz),url(r'^Api_save/',Api_save),
#     url(r"^get_api_data/",get_api_data),url(r"^Api_send/",Api_send),url(r'^copy_api/',copy_api)
# ]