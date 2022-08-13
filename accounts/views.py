
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.models import User
from .forms import *
from django.contrib import messages
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from accounts.mixins import AdminAccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
# ------------------------------ Login View ------------------------------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:panel')
    context = {}
    template_name = "accounts/login.html"
    form = LoginForm(request.POST or None)
    if 'next' in request.GET:
        request.session['next'] = request.GET['next']

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.session:
                    return redirect(request.session['next'])
                return redirect('accounts:panel')
        context["error"] = True
    context["form"] = form

    return render(request, template_name, context)

class UserCreateView(SuccessMessageMixin, generic.CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = SignupForm
    success_message = 'کاربر جدید با موفقیت ایجاد گردید.'
    success_url = reverse_lazy('accounts:panel')
    
class Panel(LoginRequiredMixin, generic.TemplateView):
    pass