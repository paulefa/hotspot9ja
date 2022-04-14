from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('hotspotapp:profile')
    template_name = 'registration/signup.html'
    
# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('hotspotapp:dashboard')
    template_name = 'registration/profile.html'