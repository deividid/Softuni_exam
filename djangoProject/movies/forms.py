from django import forms

from movies.mixins import PlaceHolderMixin, ReadOnlyMixin
from movies.models import Movie, Director, Studios, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['uploaded_by',]
        
        
class CreateMovieForm(PlaceHolderMixin, MovieForm):
    pass


class EditMovieForm(PlaceHolderMixin, MovieForm):
    pass


class DeleteMovieForm(ReadOnlyMixin, MovieForm):
    pass


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        exclude = ('uploaded_by',)


class CreateDirectorForm(PlaceHolderMixin, DirectorForm):
    pass


class EditDirectorForm(PlaceHolderMixin, DirectorForm):
    pass


class DeleteDirectorForm(ReadOnlyMixin, DirectorForm):
    pass


class StudiosForm(forms.ModelForm):
    class Meta:
        model = Studios
        exclude = ('uploaded_by',)


class CreateStudiosForm(PlaceHolderMixin, StudiosForm):
    pass


class EditStudiosForm(PlaceHolderMixin, StudiosForm):
    pass


class DeleteStudiosForm(ReadOnlyMixin, StudiosForm):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['uploaded_by', 'to_movie', 'user']


class CreateCommentForm(PlaceHolderMixin, CommentForm):
    pass


class EditCommentForm(PlaceHolderMixin, CommentForm):
    pass


class DeleteCommentForm(ReadOnlyMixin, CommentForm):
    pass

