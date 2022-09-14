from msilib.schema import Error
from turtle import title
from django.shortcuts import render, redirect
from django.contrib import messages

from login.models import isUserLoggedIn, redirectToLogin
from .models import *
# Create your views here.
def viewMember(Request, memberId):
    member = Member.objects.get(id = memberId)
    return render(Request, 'members/member-details.html', { 'member': member })

def deleteMember(Request, memberId):
    return Member.deleteMember(Request, memberId)

def navigateToMemberSearch(Request):
    return render(Request, 'members/member-profile.html')

def navigateToMemberPage(Request):
    return render(Request, 'members/member-page.html', {'memberPage': True})

def addMember(Request):
    return Member.addUpdateMember(Request)

def performSearchQuery(Request):
    return Member.searchMember(Request)

def updateMember(Request):
    return Member.addUpdateMember(Request)

def navigateToDatabase(Request):
    memberList = Member.objects.all()
    context = {
        'memberList': memberList,
        'membercount': memberList.count(),
        'isDataBase': True,
    }
    return render(Request, 'members/member-database.html', context)




