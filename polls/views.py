from django.urls import reverse
from .models import Question, Choice

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    lastest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        # * La variable ahora está disponible en index.html
        "lastest_question_list": lastest_question_list
    })


def detail(request, questions_id):
    question= get_object_or_404(Question, pk=questions_id)
    return render(request, "polls/detail.html", {"question":question} )

def results(request, questions_id):
    return HttpResponse(F"Estás viendo la pregunta {questions_id}"  )


def vote(request, questions_id):
    question= get_object_or_404(Question,pk=questions_id  )
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    
    except(KeyError, Choice.DoesNotExist ):
        return render(request, "polls/detail.html", {"question": question, "error_message": "No elegiste alguna opción"})

        
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

  