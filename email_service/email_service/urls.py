from django.conf.urls import url
from django.contrib import admin
import emailer.views as views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^newsletter/create/$', views.create_newsletter, name='create-newsletter'),
    url(r'^ajax/create_newsletter/$', views.ajax_create_newsletter, name='ajax-create-newsletter'),
    url(r'^newsletter/send/$', views.send_newsletter, name='send-newsletter'),
    url(r'^subscribers/$', views.subscribers, name='subscribers'),
    url(r'^newsletter/(?P<newsletter_id>\d+)/stats/$', views.newsletter_stat, name='newsletter-stat'),
    url(r'^newsletter/open/(?P<newsletter_id>\d+)/$', views.open_track, name='open-track'),
]