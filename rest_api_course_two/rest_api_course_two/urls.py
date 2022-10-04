from django.contrib import admin
from django.urls import path
from RestApi.views import worker_list,detail_workers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('workers/',worker_list),
    path('workers/<int:pk>/',detail_workers),
]


# Getting a Json File
urlpatterns = format_suffix_patterns(urlpatterns)