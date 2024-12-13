from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import BaseFormView

from albums.models import Album
from prep.utils import get_profile
from profiles.forms import ProfileForm, DeleteProfileForm
from profiles.models import Profile


# Create your views here.
class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_profile()
        if profile:
            return ["profiles/home-with-profile.html"]

        return ["profiles/home-no-profile.html"]

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DetailsProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(DeleteView):

    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_profile()
