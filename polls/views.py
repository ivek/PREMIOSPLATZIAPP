from django.views.generic import ListView
from django.views import generic
from django.utils import timezone

from django.urls import reverse
from .models import Question, Choice

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
'''def index(request):
    lastest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        # * La variable ahora está disponible en index.html
        "lastest_question_list": lastest_question_list
    })


def detail(request, questions_id):
    question= get_object_or_404(Question, pk=questions_id)
    return render(request, "polls/detail.html", {"question":question} )

def results(request, questions_id):
    question= get_object_or_404(Question, pk=questions_id)
    return render(request, "polls/results.html", {"question":question} )'''

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name="lastest_question_list"

    def get_queryset(self):
        '''return the last five published questions'''
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class ResultView(generic.DetailView):
    model = Question
    template_name='polls/results.html'

class DetailView(generic.DetailView):
    model = Question
    template_name='polls/detail.html'

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

  