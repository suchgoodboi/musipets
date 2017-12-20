from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.SongIndexView.as_view(), name='index'),
    url(r'^new/$', views.RegisterSongView.as_view()),
    url(r'^search/$', views.SearchView.as_view()),
    url(r'^novo/$', views.RegisterSongView.as_view(), name='register'),
    url(r'^busca/$', views.SearchView.as_view(), name='search'),
    url(r'^atualizar-cadastro/(?P<request_key>\w+)/$', views.update_register, name='update_register'),
    url(r'^pet/(?P<slug>[-\w]*)/foto/$', views.upload_image, name='upload_image'),
    url(r'^(?P<slug>[-\w]*)/editar/$', views.EditSongView.as_view(), name='edit'),
    url(r'^(?P<slug>[-\w]*)/poster/$', views.poster, name='poster'),
    url(r'^(?P<slug>[-\w]*)/editar/situacao/$', views.change_status, name='change_status'),
    url(r'^(?P<slug>[-\w]*)/deletar/$', views.delete_song, name='delete_pet'),
    url(r'^(?P<slug>[-\w]*)/registrado/$', views.registered, name='registered'),

    url(r'^(?P<pk_or_slug>[-\w]*)/$', views.song_detail_view, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.song_detail_view, name='detail_by_pk'),
]