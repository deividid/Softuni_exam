from django.urls import path, include

from movies import views


urlpatterns = [
    path('', views.ShowMoviesView.as_view(), name='movies'),
    path('directors/', views.ShowDirectorsView.as_view(), name='directors'),
    path('studios/', views.ShowStudiosView.as_view(), name='studios'),
    path('create_movie/', views.CreateMovieView.as_view(), name='create_movie'),
    path('add_director/', views.CreateDirectorView.as_view(), name='add_director'),
    path('add_studio/', views.CreateStudioView.as_view(), name='add_studio'),
    path('<int:pk>/', include([
        path('edit_movie/', views.EditMovieView.as_view(), name='edit_movie'),
        path('edit_director/', views.EditDirectorView.as_view(), name='edit_director'),
        path('edit_studio/', views.EditStudioView.as_view(), name='edit_studio'),
        path('delete_movie/', views.DeleteMovieView.as_view(), name='delete_movie'),
        path('delete_director/', views.DeleteDirectorView.as_view(), name='delete_director'),
        path('delete_studio/', views.DeleteStudioView.as_view(), name='delete_studio'),
        path('comments/', views.view_comments, name='comments'),
        path('create_comment/', views.CreateCommentView.as_view(), name='create_comment'),
        path('edit_comment/', views.EditCommentView.as_view(), name='edit_comment'),
        path('delete_comment', views.DeleteCommentView.as_view(), name='delete_comment'),
   ]))
]
