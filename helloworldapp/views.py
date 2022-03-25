from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wishes(request):
    return render(request,'hello.html')

def msg(request):
    return HttpResponse("hello siva good afternoon")
    
