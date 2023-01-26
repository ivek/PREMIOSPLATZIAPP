from django.contrib import admin

from polls.models import Choice, Question

#admpliar admin


# Register your models here.

admin.site.register([Question,Choice])
