from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^pets/$', views.ListSongs.as_view(), name='list_songs'),
    url(r'^cities/$', views.GroupList.as_view(), name='list_song'),
]
