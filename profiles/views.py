from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from registration.models import Profile
from django.contrib.auth.models import User

class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 10
    queryset = Profile.objects.select_related('user').all()

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
