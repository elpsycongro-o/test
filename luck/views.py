from django.shortcuts import render

def index(request):
    return render(request,"luck/index.html")
