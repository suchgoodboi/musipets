from rest_framework import generics

from api import serializers
from meupet.models import Song, Group


class GroupList(generics.ListAPIView):
    serializer_class = serializers.GroupSerializer

    def get_queryset(self):
        queryset = Group.objects.all()
        group = self.request.query_params.get('group', None)
        if group:
            queryset = queryset.filter(search_name__startswith=group)
        return queryset


class ListSongs(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer
