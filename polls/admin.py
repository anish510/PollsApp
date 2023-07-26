from django.contrib import admin
from .models import Question,choice


# Register your models here.
#to put the models in the same admin directory

class ChoiceInlinie(admin.TabularInline):
    model = choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    
    list_display = ["question_text", "pub_date"]
    inlines = [ChoiceInlinie]
    
admin.site.register(Question, QuestionAdmin)
    