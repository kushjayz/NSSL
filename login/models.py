from django.db import models
from django.shortcuts import redirect
from django.contrib import messages

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

def isUserLoggedIn(request):
    if 'isAdminLoggedIn' in request.session:
        if request.session['isAdminLoggedIn'] == True :
            return True
    else:
        return False
        # messages.info(request,'User session failed, Please login')
        # return redirect('login')

def redirectToLogin(request, *args, **kwargs):
    if args:
        for msg in args:
            messages.info(request, msg)
        return redirect('login')
    else:
        messages.info(request,'User session failed, Please login')
        return redirect('login')

