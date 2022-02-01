from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from .forms import SignupForm

login = LoginView.as_view(template_name="accounts/login_form.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "회원가입 환영합니다.")
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {'form': form, })
