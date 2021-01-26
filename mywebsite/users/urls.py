from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ProfilePageView, EditProfilePageView, CreateProfilePageView
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile-page'),
    path('<int:pk>/edit-profile-page/',
         EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create-profile-page/',
         CreateProfilePageView.as_view(), name='create-profile-page'),
]
