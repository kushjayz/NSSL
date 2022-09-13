import datetime
from multiprocessing import context
from django.db import models
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your models here.
class Member(models.Model):
    memberId = models.CharField(max_length=200, null=True)
    passportNic = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    disabilities = models.CharField(max_length=200, null=True)
    emergencyContactNumber = models.CharField(max_length=200, null=True)
    dateOfBirth = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True)
    houseAptNo = models.CharField(max_length=200, null=True)
    lane = models.CharField(max_length=200, null=True)
    road = models.CharField(max_length=200, null=True)
    subArea = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    province = models.CharField(max_length=200, null=True)
    occupation = models.CharField(max_length=200, null=True)
    contactNumber = models.CharField(max_length=200, null=True)
    emergencyContact = models.CharField(max_length=200, null=True)
    gojukaiStatus = models.CharField(max_length=200, null=True)
    gojukaiReceivedDate = models.CharField(max_length=200, null=True)
    sponsorMembershipNo = models.CharField(max_length=200, null=True)
    sponsorRelationship = models.CharField(max_length=200, null=True)
    tozanHistory = models.CharField(max_length=200, null=True)
    gojukaiVenue = models.CharField(max_length=200, null=True)
    gohonzonStatus = models.CharField(max_length=200, null=True)
    gohonzonReceivedDate = models.CharField(max_length=200, null=True)
    gohonzonVenue = models.CharField(max_length=200, null=True)
    nameOftheSponsor = models.CharField(max_length=200, null=True)
    addressOfSponsor = models.CharField(max_length=200, null=True)
    sponsorContactNumber = models.CharField(max_length=200, null=True)

    def searchMember(Request):
        error = True
        unableToFilter = False
        if Request.method == 'POST':
                if 'membershipNumber' in Request.POST :
                        membershipNumber = Request.POST.get('membershipNumber','')
                        filteredMember = Member.objects.filter(memberId__icontains = membershipNumber)
                        if filteredMember:
                                return Member.searchAndredirect(Request, filteredMember.first())
                        else:
                                unableToFilter = True
                
                if 'nicPassportNumber' in Request.POST :
                        nicPassportNumber = Request.POST.get('nicPassportNumber','')
                        filteredMember = Member.objects.filter(passportNic__icontains = nicPassportNumber)
                        if filteredMember:
                                return Member.searchAndredirect(Request, filteredMember.first())
                        else:
                                unableToFilter = True

                if 'contactNumber' in Request.POST :
                        contactNumber = Request.POST.get('contactNumber','')
                        filteredMember = Member.objects.filter(contactNumber__icontains = contactNumber)
                        if filteredMember:
                                return Member.searchAndredirect(Request, filteredMember.first())
                        else:
                                unableToFilter = True
        if unableToFilter:
                messages.info(Request, 'There are no users with the specified filters!')
                return redirect('navigate-to-search')
        elif error :
                messages.info(Request, 'Fill atleast one of the fields to search!')
                return redirect('navigate-to-search')


    def searchAndredirect(Request, searchedMember):
        context = {
                'memberPage': True,
                'title': searchedMember.name,
                'member': searchedMember,
        }

        # if searchedMember.gohonzonReceivedDate:
        #         context['gohonzonDate'] = datetime.datetime.strptime(searchedMember.gohonzonReceivedDate, '%d/%m/%Y').strftime('%Y-%m-%d')
        
        # if searchedMember.gojukaiReceivedDate:
        #         context['gojukaiDate'] = datetime.datetime.strptime(searchedMember.gojukaiReceivedDate, '%d/%m/%Y').strftime('%Y-%m-%d')
        return render(Request, 'members/member-page.html', context)


    def addUpdateMember(Request):
        error = False
        if Request.method == 'POST':
                if 'membershipNumber' in Request.POST :
                        membershipNumber = Request.POST.get('membershipNumber','')
                else :
                        error = True

                if 'fullName' in Request.POST:
                        fullName = Request.POST.get('fullName','')
                else :
                        error = True

                if 'phoneNumber' in Request.POST:
                        phoneNumber = Request.POST.get('phoneNumber','')
                else :
                        error = True

                if 'passportNic' in Request.POST:
                        passportNic = Request.POST.get('passportNic','')
                else :
                        error = True
                
                if 'address' in Request.POST:
                        address = Request.POST.get('address','')

                if 'disabilities' in Request.POST:
                        disabilities = Request.POST.get('disabilities','')

                if 'occupation' in Request.POST:
                        occupation = Request.POST.get('occupation','')

                if 'emergencyContact' in Request.POST:
                        emergencyContact = Request.POST.get('emergencyContact','')

                if 'emergencyContactNumber' in Request.POST:
                        emergencyContactNumber = Request.POST.get('emergencyContactNumber','')

                if 'gojukaiStatus' in Request.POST:
                        gojukaiStatus = Request.POST.get('gojukaiStatus','')

                if 'gojukaiDate' in Request.POST:
                        gojukaiDate = Request.POST.get('gojukaiDate','')

                if 'gojukaiVenue' in Request.POST:
                        gojukaiVenue = Request.POST.get('gojukaiVenue','')
                        
                if 'gohonzonStatus' in Request.POST:
                        gohonzonStatus = Request.POST.get('gohonzonStatus','')

                if 'gohonzonDate' in Request.POST:
                        gohonzonDate = Request.POST.get('gohonzonDate','')

                if 'gohonzonVenue' in Request.POST:
                        gohonzonVenue = Request.POST.get('gohonzonVenue','')

                if 'sponsorMembershipNo' in Request.POST:
                        sponsorMembershipNo = Request.POST.get('sponsorMembershipNo','')

                if 'sponsorName' in Request.POST:
                        sponsorName = Request.POST.get('sponsorName','')

                if 'sponsorRelationship' in Request.POST:
                        sponsorRelationship = Request.POST.get('sponsorRelationship','')

                if 'tozanHistory' in Request.POST:
                        tozanHistory = Request.POST.get('tozanHistory','')
                        
                if error:
                        messages.info(Request,'Required fields were not filled!')
                        return redirect('navigate-to-member-details')
                else:
                        newMemberObj = Member (
                        memberId = membershipNumber,
                        name = fullName,
                        passportNic = passportNic,
                        occupation = occupation,
                        contactNumber = phoneNumber,
                        address = address,
                        emergencyContact = emergencyContact,
                        emergencyContactNumber = emergencyContactNumber,
                        disabilities = disabilities,
                        gojukaiStatus = gojukaiStatus,
                        gojukaiReceivedDate = gojukaiDate,
                        sponsorMembershipNo = sponsorMembershipNo,
                        nameOftheSponsor = sponsorName,
                        sponsorRelationship = sponsorRelationship,
                        tozanHistory = tozanHistory,
                        gojukaiVenue = gojukaiVenue,
                        gohonzonStatus = gohonzonStatus,
                        gohonzonReceivedDate = gohonzonDate,
                        gohonzonVenue = gohonzonVenue,
                        )
                        newMemberObj.save()
                        messages.info(Request,'Member has been saved successfully!')
                        messages.info(Request,'Check in the member database!')
                        return redirect('home')

