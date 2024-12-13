from django.urls import path, include

from profiles import views
from profiles.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('profile/', include([
        path('details/', views.DetailsProfileView.as_view(), name='profile-details'),
        path('delete/', views.DeleteProfileView.as_view(), name='profile-delete'),
    ])),
]