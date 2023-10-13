from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class CustomLoginView(LoginView):
    template_name = 'login.html'

@login_required
def post_login(request):
    response = HttpResponse('Logged In!', content_type='text/plain')
    return response
