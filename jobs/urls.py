from django.conf.urls import url
from . import views

app_name = 'jobs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/(?P<username>\w+)/$', views.user_profile, name='user_profile'),
    url(r'^offers/$', views.job_offers, name='job_offers'),

]