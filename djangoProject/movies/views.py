from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import BaseFormView

from accounts.models import CustomUser
from movies.forms import MovieForm, DirectorForm, StudiosForm, CreateMovieForm, CreateDirectorForm, CreateStudiosForm, \
    EditStudiosForm, EditMovieForm, EditDirectorForm, DeleteMovieForm, DeleteDirectorForm, DeleteStudiosForm, \
    CommentForm, EditCommentForm, DeleteCommentForm
from movies.models import Movie, Director, Studios, Comment


# Create your views here.


class ShowMoviesView(ListView, BaseFormView):
    model = Movie
    form_class = MovieForm
    template_name = 'base.html'

    def form_valid(self, form):
        form.save()
        super().form_valid(form)


class CreateMovieView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = CreateMovieForm
    template_name = 'movies/create_movie.html'
    success_url = reverse_lazy('movies')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class EditMovieView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = EditMovieForm
    template_name = 'movies/edit_movie.html'
    success_url = reverse_lazy('movies')


class DeleteMovieView(LoginRequiredMixin, DeleteView):
    model = Movie
    form_class = DeleteMovieForm
    template_name = 'movies/delete_movie.html'
    success_url = reverse_lazy('movies')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class ShowDirectorsView(ListView, BaseFormView):
    model = Director
    form_class = DirectorForm
    template_name = 'directors/directors.html'

    def form_valid(self, form):
        form.save()
        super().form_valid(form)


class CreateDirectorView(LoginRequiredMixin, CreateView):
    model = Director
    form_class = CreateDirectorForm
    template_name = 'directors/add_director.html'
    success_url = reverse_lazy('directors')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class EditDirectorView(LoginRequiredMixin, UpdateView):
    model = Director
    form_class = EditDirectorForm
    template_name = 'directors/edit_director.html'
    success_url = reverse_lazy('directors')


class DeleteDirectorView(LoginRequiredMixin, DeleteView):
    model = Director
    form_class = DeleteDirectorForm
    template_name = 'directors/delete_director.html'
    success_url = reverse_lazy('directors')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class ShowStudiosView(ListView, BaseFormView):
    model = Studios
    form_class = StudiosForm
    template_name = 'studios/studios.html'

    def form_valid(self, form):
        form.save()
        super().form_valid(form)


class CreateStudioView(LoginRequiredMixin, CreateView):
    model = Studios
    form_class = CreateStudiosForm
    template_name = 'studios/add_studio.html'
    success_url = reverse_lazy('studios')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class EditStudioView(LoginRequiredMixin, UpdateView):
    model = Studios
    form_class = EditStudiosForm
    template_name = 'studios/edit_studio.html'
    success_url = reverse_lazy('studios')


class DeleteStudioView(LoginRequiredMixin, DeleteView):
    model = Studios
    form_class = DeleteStudiosForm
    template_name = 'studios/delete_studio.html'
    success_url = reverse_lazy('studios')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


def view_comments(request, pk):
    right_movie = Movie.objects.get(pk=pk)
    all_comments = right_movie.get_comments

    return render(request, 'comments/comments.html', {
        'comments': all_comments,
        'movie': right_movie
    })


class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/create_comment.html'

    def get_absolute_url(self):
        return f'/{self.object.pk}/comments/'

    def form_valid(self, form):
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)
        form.instance.to_movie = movie
        form.instance.user = self.request.user
        form.save()
        return redirect('comments', pk=pk)


class EditCommentView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = EditCommentForm
    template_name = 'comments/edit_comment.html'
    success_url = reverse_lazy('movies')


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    form_class = DeleteCommentForm
    template_name = 'comments/delete_comment.html'
    success_url = reverse_lazy('movies')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

