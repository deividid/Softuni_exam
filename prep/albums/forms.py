from django import forms

from albums.models import Album
from prep.mixins import PlaceHolderMixin, ReadOnlyMixin


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner', )


class CreateAlbumForm(PlaceHolderMixin, AlbumForm):
    pass


class EditAlbumForm(PlaceHolderMixin, AlbumForm):
    pass


class DeleteAlbumForm(ReadOnlyMixin, AlbumForm):
    readonly_fields = ['album_name', 'artist', 'description', 'genre', 'price']
