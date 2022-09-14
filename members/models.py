import datetime
from multiprocessing import context
from django.db import models
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your models here.
class Member(models.Model):
    memberId = models.CharField(max_length=200, unique=True)
    passportNic = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    disabilities = models.CharField(max_length=200, null=True, default='--')
    emergencyContactNumber = models.CharField(max_length=200, null=True, default='--')
    dateOfBirth = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True, default='--')
    houseAptNo = models.CharField(max_length=200, null=True, default='--')
    lane = models.CharField(max_length=200, null=True, default='--')
    road = models.CharField(max_length=200, null=True, default='--')
    subArea = models.CharField(max_length=200, null=True, default='--')
    city = models.CharField(max_length=200, null=True, default='--')
    district = models.CharField(max_length=200, null=True, default='--')
    province = models.CharField(max_length=200, null=True, default='--')
    occupation = models.CharField(max_length=200, null=True)
    contactNumber = models.CharField(max_length=200, null=True, default='--')
    emergencyContact = models.CharField(max_length=200, null=True, default='--')
    gojukaiStatus = models.CharField(max_length=200, null=True, default='No')
    gojukaiReceivedDate = models.CharField(max_length=200, null=True)
    sponsorMembershipNo = models.CharField(max_length=200, null=True)
    sponsorRelationship = models.CharField(max_length=200, null=True)
    tozanHistory = models.CharField(max_length=200, null=True, default='--')
    gojukaiVenue = models.CharField(max_length=200, null=True)
    gohonzonStatus = models.CharField(max_length=200, null=True, default='No')
    gohonzonReceivedDate = models.CharField(max_length=200, null=True)
    gohonzonVenue = models.CharField(max_length=200, null=True)
    nameOftheSponsor = models.CharField(max_length=200, null=True)
    addressOfSponsor = models.CharField(max_length=200, null=True)
    sponsorContactNumber = models.CharField(max_length=200, null=True)

    def deleteMember(Request, memberId):
        member = Member.objects.get(id = memberId)
        if member:
                isDeleted = member.delete()
                if isDeleted:
                        messages.info(Request,'Member with id : ' + member.memberId + ' was removed successfully')
                        return redirect('home')
        else:
                messages.info('Error occured when removing member!')
                messages.info('Could not find user! Please try again !')
                return redirect('home')

    def searchMember(Request):
        error = True
        unableToFilter = False
        if Request.method == 'POST':
                if 'membershipNumber' in Request.POST :
                        membershipNumber = Request.POST.get('membershipNumber','')
                        if membershipNumber:
                                filteredMember = Member.objects.filter(memberId__icontains = membershipNumber)
                                if filteredMember:
                                        return Member.searchAndredirect(Request, filteredMember.first())
                                else:
                                        unableToFilter = True
                
                if 'nicPassportNumber' in Request.POST :
                        nicPassportNumber = Request.POST.get('nicPassportNumber','')
                        if nicPassportNumber:
                                filteredMember = Member.objects.filter(passportNic__icontains = nicPassportNumber)
                                if filteredMember:
                                        return Member.searchAndredirect(Request, filteredMember.first())
                                else:
                                        unableToFilter = True

                if 'contactNumber' in Request.POST :
                        contactNumber = Request.POST.get('contactNumber','')
                        if contactNumber:
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
        return render(Request, 'members/member-page.html', context)


    def addUpdateMember(Request):
        error = False
        isUpdatePerformed = False
        if Request.method == 'POST':
                if 'id' in Request.POST :
                        id = Request.POST.get('id','')
                        isUpdatePerformed = True

                if 'membershipNumber' in Request.POST :
                        membershipNumber = Request.POST.get('membershipNumber','')
                else :
                        error = True

                if 'fullName' in Request.POST:
                        fullName = Request.POST.get('fullName','')
                else :
                        error = True

                if 'gender' in Request.POST:
                        gender = Request.POST.get('gender','')
                
                if 'dateOfBirth' in Request.POST:
                        dateOfBirth = Request.POST.get('dateOfBirth','')
                else :
                        error = True

                if 'phoneNumber' in Request.POST:
                        phoneNumber = Request.POST.get('phoneNumber','')
                else :
                        error = True

                if 'passportNic' in Request.POST:
                        passportNic = Request.POST.get('passportNic','')
                
                if 'address' in Request.POST:
                        address = Request.POST.get('address','')

                if 'disabilities' in Request.POST:
                        disabilities = Request.POST.get('disabilities','')

                if 'occupation' in Request.POST:
                        occupation = Request.POST.get('occupation','')

                if 'emergencyContact' in Request.POST:
                        emergencyContact = Request.POST.get('emergencyContact','')
                else :
                        error = True

                if 'emergencyContactNumber' in Request.POST:
                        emergencyContactNumber = Request.POST.get('emergencyContactNumber','')
                else :
                        error = True

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
                elif isUpdatePerformed:
                        fetchedMember = Member.objects.get(id = id)
                        if fetchedMember:
                                fetchedMember.memberId = membershipNumber
                                fetchedMember.name = fullName
                                fetchedMember.gender = gender
                                fetchedMember.dateOfBirth = dateOfBirth
                                fetchedMember.passportNic = passportNic
                                fetchedMember.occupation = occupation
                                fetchedMember.contactNumber = phoneNumber
                                fetchedMember.address = address
                                fetchedMember.emergencyContact = emergencyContact
                                fetchedMember.emergencyContactNumber = emergencyContactNumber
                                fetchedMember.disabilities = disabilities
                                fetchedMember.gojukaiStatus = gojukaiStatus
                                fetchedMember.gojukaiReceivedDate = gojukaiDate
                                fetchedMember.sponsorMembershipNo = sponsorMembershipNo
                                fetchedMember.nameOftheSponsor = sponsorName
                                fetchedMember.sponsorRelationship = sponsorRelationship
                                fetchedMember.tozanHistory = tozanHistory
                                fetchedMember.gojukaiVenue = gojukaiVenue
                                fetchedMember.gohonzonStatus = gohonzonStatus
                                fetchedMember.gohonzonReceivedDate = gohonzonDate
                                fetchedMember.gohonzonVenue = gohonzonVenue

                                fetchedMember.save()
                                messages.info(Request,'Member details was updated successfully!')
                                messages.info(Request,'Member reference number:' + membershipNumber )
                                return redirect('home')

                else:
                        newMemberObj = Member (
                        memberId = membershipNumber,
                        name = fullName,
                        gender = gender,
                        dateOfBirth = dateOfBirth,
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
                        messages.info(Request,'Member details have been saved successfully!')
                        messages.info(Request,'Member reference number:' + membershipNumber )
                        return redirect('home')


