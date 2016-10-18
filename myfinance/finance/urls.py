from django.conf.urls import url
from finance.views import hello_world, return_back

urlpatterns = [
                url(r'^$', hello_world),
                url(r'^charges/$', return_back)
              ]