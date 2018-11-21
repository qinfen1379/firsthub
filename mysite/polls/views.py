from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import Question
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def test(request):
    return HttpResponse("this is test view")

def testyear(request,year):
    raise Http404("this is 404 error")
    # return HttpResponse("this is testyear {} view".format(year))

def detail(request,question_id):
    return HttpResponse("question_id is {}".format(question_id))