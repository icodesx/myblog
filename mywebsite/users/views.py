from django.db import models
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, UpdateView, CreateView
from blogapp.models import Profile
from .forms import ProfilePageForm

# Create your views here.


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create-profile-page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit-profile-page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'github_url']
    success_url = reverse_lazy('index')


class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user-profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(
            *args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('index')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
