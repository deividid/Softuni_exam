from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CustomUserCreationForm


# Create your views here.
class CreateUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('movies')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class CustomUserLoginView(LoginView):
    template_name = 'users/user_login.html'





