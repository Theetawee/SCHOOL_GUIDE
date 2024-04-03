from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from accounts.forms import SignupForm

# Create your views here.

def signup_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    context={}
    if request.POST:
        form =SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password1')
            account=authenticate(email=email,password=password)
            login(request,account)
            return redirect('home')
        else:
            context['form']=form
    else:
        form =SignupForm()
        
    context['form']=form
    
    return render(request,'accounts/signup.html',context)


def logout_user(request):
    logout(request)
    
    return redirect('home')