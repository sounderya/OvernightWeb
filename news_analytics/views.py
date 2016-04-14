from django.shortcuts import render
import json
from django.http import HttpResponse
import search_call as sc

# Create your views here.
def landing_page(request):
    return render(request, 'landingpage.html')

# api call to alchemy to get content
def get_content(request):
    print "here"
    res = ''
    if request.method == 'POST':
        params = request.POST
        val = params.get('search_keyword')
        print val
        res = sc.getNews(val)
        print "outside"
    # return HttpResponse(json.dumps({'data': res}), content_type="application/json")
    return render(request, 'landingpage.html', {'data': res})
def showSearchresult(request):
    return render(request,'searchresults_bali.html')



def login (request):
    return render(request,'login.html')


def signup (request):
    return render(request,'signup.html')

def showBookingPage(request):
    return render(request, 'bookingdetails.html')

def showBookingConfirmation(request):
    return render(request, 'bookingconfirmation.html')

def showUserProfile(request):
    return render(request, 'user-profile.html')

def showUserProfileBookingHistory(request):
    return render(request, 'user-profile-booking-history.html')

def showUserProfileCards(request):
    return render(request, 'user-profile-cards.html')

def showUserProfileSettings(request):
    return render(request, 'user-profile-settings.html')