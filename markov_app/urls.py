from django.conf.urls import *
from markov_app import views

urlpatterns = [url(r'^$', views.HomePageView.as_view(), name='Home View'),
               url(r'^$', views.Database, name='database_update'),
]
