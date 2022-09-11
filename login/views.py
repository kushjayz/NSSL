from django.shortcuts import render, redirect
from .models import Admin, isUserLoggedIn, redirectToLogin
from django.contrib import messages

# Create your views here.
def loadLogin(Request):
    return render(Request, 'login/login.html')

def verifyLogin(request):

    error = False
    if request.method == 'POST':
        enteredUN = request.POST.get('username')
        enteredPW = request.POST.get('password')
        admin = Admin.objects.filter(username = enteredUN, password = enteredPW)
        if admin:
            request.session['isAdminLoggedIn'] = True
            return redirect('home')
        else :
            messages.info(request,'Invalid username or password !')
            return redirect('login')
    else:
        error = True
    
    if error:
        messages.info(request,'Error has occured! No POST values ')
        return redirect('login')

def home(Request):
    if isUserLoggedIn(Request) == True:
        return render(Request, 'login/home.html')
    else:
        return redirectToLogin(Request)