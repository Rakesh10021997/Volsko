from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from testapp.forms import SignUpForm
# Create your views here.

def Home(request):
    return render(request,'testapp/home.html')

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.form)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('accounts/login')
    return render(request,'testapp/signup.html',{'form':form})

@login_required
def Volsko(request):
    return render(request,'testapp/volsko.html')

def log_out(request):
    return render(request,'testapp/logout.html')
