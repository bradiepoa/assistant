from django.shortcuts import render
# Create your views here.

def loginViews(request):
    return render(request, 'accounts/login.html')


def registerViews(request):
    return render(request, 'accounts/register.html')





def forgotViews(request):
    return render(request, 'accounts/forgot.html')
