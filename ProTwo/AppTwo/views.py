from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    helper_lst = {'help_me': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=helper_lst)
