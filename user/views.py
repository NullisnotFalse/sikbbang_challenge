from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import UserModel
# Create your views here.

def sign_up_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():  # 2
            print("save")
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password1 = request.POST.get('password_check1', '')
            password2 = request.POST.get('password_check2', '')

            if password1 ==password2:
                UserModel.objects.create_user(username=username,password=password1,email=email)
        else:
            print(form.errors)
    else:
        pass
    form = SignUpForm()
    print(form)
    return render(request, 'user/signup.html', {'form': form})