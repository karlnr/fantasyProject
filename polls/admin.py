from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Choice, Question

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # You’ll follow this pattern – create a model admin class, then pass it as the second argument
    # to admin.site.register() – any time you need to change the admin options for a model.

    # fields = ['pub_date', 'question_text']

    # adds sectio  header
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)