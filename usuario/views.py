from django.shortcuts import render

def fuser(request):
    return render(request, 'foruser.html')