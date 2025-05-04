from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_display = ('question_text', 'pub_date', 'display_choices', 'was_published_recently')
    def display_choices(self, obj):
        return ", ".join(choice.choice_text for choice in obj.choice_set.all())
    display_choices.short_description = 'Choices'
    
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    
    
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'display_choices')
    
#     def display_choices(self, obj):
#         return ", ".join(choice.choice_text for choice in obj.choice_set.all())
#     display_choices.short_description = 'Choices'
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question')

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)