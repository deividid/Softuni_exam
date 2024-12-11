from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('create_user/', views.CreateUserView.as_view(), name='create_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.CustomUserLoginView.as_view(), name='login'),

]
