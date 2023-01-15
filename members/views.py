from django.shortcuts import render
from login.models import isUserLoggedIn, redirectToLogin
from .models import *
# Create your views here.
def viewMember(Request, memberId):
    if isUserLoggedIn(Request) == True:
        member = Member.objects.get(id = memberId)
        return render(Request, 'members/member-details.html', { 'member': member })
    else:
        return redirectToLogin(Request)

def deleteMember(Request, memberId):
    if isUserLoggedIn(Request) == True:
        return Member.deleteMember(Request, memberId)
    else:
        return redirectToLogin(Request)

def navigateToMemberSearch(Request):
    if isUserLoggedIn(Request) == True:
        return render(Request, 'members/member-profile.html')
    else:
        return redirectToLogin(Request)

def navigateToMemberPage(Request):
    if isUserLoggedIn(Request) == True:
        return render(Request, 'members/member-page.html', {'memberPage': True})
    else:
        return redirectToLogin(Request)

def addMember(Request):
    if isUserLoggedIn(Request) == True:
        return Member.addUpdateMember(Request)
    else:
        return redirectToLogin(Request)

def performSearchQuery(Request):
    if isUserLoggedIn(Request) == True:
        return Member.searchMember(Request)
    else:
        return redirectToLogin(Request)

def updateMember(Request):
    if isUserLoggedIn(Request) == True:
        return Member.addUpdateMember(Request)
    else:
        return redirectToLogin(Request)

def navigateToDatabase(Request):
    if isUserLoggedIn(Request) == True:
        memberList = Member.objects.all()
        context = {
            'memberList': memberList,
            'membercount': memberList.count(),
            'isDataBase': True,
        }
        return render(Request, 'members/member-database.html', context)
    else:
        return redirectToLogin(Request)




