from django.shortcuts import render

# Create your views here.

def nick(request):
    return render (request, 'jobs/home.html')
