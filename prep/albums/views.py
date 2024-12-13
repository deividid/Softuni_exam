from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from albums.forms import AlbumForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from albums.models import Album
from prep.utils import get_profile


# Create your views here.

class AlbumCreateView(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)


class AlbumDetailView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'


class AlbumEditView(UpdateView):
    model = Album
    form_class = EditAlbumForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home')


class AlbumDeleteView(DeleteView):
    model = Album
    pk_url_kwarg = 'id'
    form_class = DeleteAlbumForm
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)



