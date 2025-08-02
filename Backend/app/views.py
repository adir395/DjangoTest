from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePage(request):
    # return HttpResponse("Home Page Respone")
    return render (request, 'homePage/homePage.html')

def testPage(request):
    # return HttpResponse("Home Page Respone")
    return render (request, 'homePage/test.html')