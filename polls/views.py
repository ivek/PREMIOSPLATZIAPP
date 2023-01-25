from .models import Question 

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    lastest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        # * La variable ahora está disponible en index.html
        "lastest_question_list": lastest_question_list
    })


def detail(request, questions_id):
    return HttpResponse(F"Estás viendo la pregunta {questions_id}"  )


def results(request, questions_id):
    return HttpResponse(F"Estás viendo la pregunta {questions_id}"  )


def vote(request, questions_id):
    return HttpResponse(F"Estás votando a la pregunta  {questions_id}"  )