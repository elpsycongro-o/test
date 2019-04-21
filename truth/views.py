from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choice 

def index(request):
    question=Question.objects.all()    
    return render(request,"truth/index.html",{"question_list":question})

