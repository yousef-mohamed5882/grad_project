from django.contrib import admin

from Q_A.models import answers, characters, questions

# Register your models here.
admin.site.register(questions)
admin.site.register(characters)
admin.site.register(answers)
