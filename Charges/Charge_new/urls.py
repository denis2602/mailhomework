from django.conf.urls import url
from Charge_new.views import user, generator

urlpatterns = [
                  url(r'^$', user),
                  url(r'^generator/$', generator),
              ]
