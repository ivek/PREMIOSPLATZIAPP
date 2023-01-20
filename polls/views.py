from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return HttpResponse ('Estás en la página principal de Premios Platzi App')


def detail(request, questions_id):
    return HttpResponse(F"Estás viendo la pregunta {questions_id}"  )


def results(request, questions_id):
    return HttpResponse(F"Estás viendo la pregunta {questions_id}"  )


def vote(request, questions_id):
    return HttpResponse(F"Estás votando a la pregunta  {questions_id}"  )