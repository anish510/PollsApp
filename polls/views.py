from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:10]
    context = {'latest_question_list':latest_question_list}
    return render(request,"index.html",context)   

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    
    return render(request,"details.html",{"question":question})   

def results(request, question_id):
    return HttpResponse("Your result is %s." %question_id)

def vote(request,question_id):
    return HttpResponse("Your vote is %s." %question_id)
    
