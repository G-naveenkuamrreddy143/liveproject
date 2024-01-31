from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def home_view(request):
    return render(request,'home.html')
@login_required
def java_view(request):
    return render(request,'java.html')
@login_required
def python_view(request):
    return render(request,'python.html')
@login_required
def csharp_view(request):
    return render(request,'csharp.html')

def logout_view(request):
    return render(request,'logout.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        print(form.save())
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    return render(request,'signup.html',{'form':form})