from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader  # add for template
from .models import Question

from django.shortcuts import render
# no longer need to import loader and HttpResponse
# (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).

def index(request):

    # #  page’s design is hard-coded in the view.
    # #  If you want to change the way the page looks, you’ll have to edit this Python code
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # # uses template, hhtpfesponse etc
    # #  loads the template called polls/index.html and passes it a context.
    # #   The context is a dictionary mapping template variable names to Python objects.
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # render shortcut rather than template w/ context, httpresp etc
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# # get method
# from django.http import Http404
# def detail(request, question_id): # updsae for render & 404
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

from django.shortcuts import get_object_or_404  #shortvut
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


