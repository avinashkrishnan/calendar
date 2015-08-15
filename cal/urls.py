

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from cal import views

urlpatterns = patterns('',
           	url(r'^$', TemplateView.as_view(template_name='index.html')),
		url(r'^eventsXML', views.eventsXML, name='eventsXML'),
		url(r'^dataprocessor', views.dataprocessor, name='dataprocessor'),
	
)

