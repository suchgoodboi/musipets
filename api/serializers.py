from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    HyperlinkedRelatedField,
    StringRelatedField,
)

from meupet.models import Song, Group
from users.models import OwnerProfile


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'genre',)


class OwnerSerializer(ModelSerializer):
    name = CharField(source='get_full_name', read_only=True)
    id = HyperlinkedRelatedField(
        view_name='users:user_profile',
        read_only=True,
    )

    class Meta:
        model = OwnerProfile
        fields = ('name', 'id',)


class SongSerializer(ModelSerializer):
    owner = OwnerSerializer()
    group = StringRelatedField()
    text = StringRelatedField()

    # status = CharField(source='get_status', read_only=True)
    # sex = CharField(source='get_sex', read_only=True)
    # size = CharField(source='get_size', read_only=True)

    id = HyperlinkedRelatedField(
        view_name='meupet:detail_by_pk',
        read_only=True
    )

    class Meta:
        model = Song
        fields = ('id', 'owner', 'group', 'name', 'photo',)