from msilib.schema import Error
from turtle import title
from django.shortcuts import render, redirect
from django.contrib import messages

from login.models import isUserLoggedIn, redirectToLogin
from .models import *
# Create your views here.
def login(Request):
    return render(Request, 'login/login.html')

def members(Request):
    memberList = Member.objects.all()
    context = {
        'memberList': memberList,
        'membercount': memberList.count(),
    }
    return render(Request, 'members/member-list.html', context)

def viewMember(Request, memberId):
    member = Member.objects.get(id = memberId)
    return render(Request, 'members/member-details.html', { 'member': member })

def deleteMember(Request, memberId):
    member = Member.objects.get(id = memberId).delete()
    if member:
        messages.info('Member with ID ' + memberId + ' deleted successfully')
        return redirect('home')
    else:
        messages.info('Error occured when removing member!')
        messages.info('Please try again !')
        return redirect('home')

def navigateToMemberSearch(Request):
    return render(Request, 'members/member-profile.html')

def navigateToMemberPage(Request):
    return render(Request, 'members/member-page.html', {'memberPage': True})

def addMember(Request):
    return Member.addUpdateMember(Request)

def performSearchQuery(Request):
    return Member.searchMember(Request)



