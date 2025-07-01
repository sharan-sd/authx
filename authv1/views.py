from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import UserAccounts
from .forms import RegisterForm, SignInForm

# Signup View
def signup(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(
                password=form.cleaned_data['password'])
            user.save()
            return render(request, "signup.html", {
                'form': RegisterForm(),
                'title': 'Sign Up',
                'signup_success': True  # This triggers the redirect in template
            })

    else:
        form = RegisterForm()

    return render(request=request, template_name="signup.html",
                  context={'title': 'Sign Up', 'form': form})

# Signin View
def signin(request):
    if request.method == "POST":      
        form = SignInForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = UserAccounts.objects.get(email=email)
                if check_password(password, user.password):
                    # Set Session
                    request.session['user_id'] = user.id
                    request.session['authenticated'] = True
                    request.session.save()
                    return redirect(to="/")
                else:
                    messages.error(request=request, message="Invalid Password")
            except UserAccounts.DoesNotExist:
                messages.error(request=request, message="Account not found")
    else:
        form = SignInForm()
    return render(request=request, template_name="signin.html",
                  context={'title': 'Sign In', 'form': form})

# Signout View
def signout(request):
    if 'user_id' in request.session:
        request.session.flush()
        messages.success(request=request, message="You have been signed out")
        return redirect(to="signin")

# Password Reset View
def password_reset(request):
    return render(request=request, template_name="reset.html",
                  context={'title': 'Reset Password'})