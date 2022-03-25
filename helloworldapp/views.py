from django.shortcuts import render

# Create your views here.
def wishes(request):
    return render(request,'hello.html')
