from django.conf.urls import patterns, url
from jizhang import views

urlpatterns = patterns('',
                url(r'^$', views.home, name = 'home')               #module.method
		       )

