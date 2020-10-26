from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from main_app.forms import CustomSignupForm

class HomeView(View):
    '''To show the Home page'''

    template_name = 'main_app/home.html'

    def get(self, request):
        return render(request, self.template_name,)

home_view = HomeView.as_view()

class UserDashboard(View):
    '''To show the UserDashboard page'''

    template_name = 'main_app/user_dashboard.html'

    def get(self, request):
        return render(request, self.template_name,)

user_dashboard = login_required(UserDashboard.as_view())
