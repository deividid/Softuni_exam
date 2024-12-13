from django.urls import path, include

from albums import views

urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name='album-add'),
    path('<int:id>/', include([
        path('details/', views.AlbumDetailView.as_view(), name='album-details'),
        path('edit/', views.AlbumEditView.as_view(), name='album-edit'),
        path('delete/', views.AlbumDeleteView.as_view(), name='album-delete')
    ])),
]