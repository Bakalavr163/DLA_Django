from django.conf.urls import url
from .views import index


urlpatterns = [
    url('1/', index, name='index'),
    url('2/', index, name='index'),
] 