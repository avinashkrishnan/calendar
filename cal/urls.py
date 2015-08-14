

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from cal import views

urlpatterns = patterns('',
           	url(r'^$', TemplateView.as_view(template_name='index.html')),
		url(r'^events', views.events, name='events'),
		url(r'^dataprocessor', views.events, name='dataprocessor'),
	
)

