from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:10]
    context = {'latest_question_list':latest_question_list}
    return render(request,"index.html",context)   

def details(request, question_id):
    return HttpResponse("The question is %s." %question_id)

def results(request, question_id):
    return HttpResponse("Your result is %s." %question_id)

def vote(request,question_id):
    return HttpResponse("Your vote is %s." %question_id)
    
