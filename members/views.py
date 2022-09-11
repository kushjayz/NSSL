from django.shortcuts import render, redirect

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
    return redirect('member-list')

def navigateToMemberSearch(Request):
    return render(Request, 'members/member-profile.html')

