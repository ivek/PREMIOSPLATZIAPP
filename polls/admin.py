from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# clase para listar nuevas respuestas
class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "questions_text"]
    inlines = [ChoiceInLine] # se agrega la clase antes creada
    list_display=("questions_text","pub_date")
    list_filter= ["pub_date"]
    search_fields=["questions_text"]


admin.site.register(Question, QuestionAdmin) # los argumentos recibidos son 
# el modelo de db y el modelo de vista