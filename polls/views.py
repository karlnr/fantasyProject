from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader  # add for template
from .models import Question

from django.shortcuts import render
# no longer need to import loader and HttpResponse
# (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).

# def index(request):
#
#     # #  page’s design is hard-coded in the view.
#     # #  If you want to change the way the page looks, you’ll have to edit this Python code
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#
#     # # uses template, hhtpfesponse etc
#     # #  loads the template called polls/index.html and passes it a context.
#     # #   The context is a dictionary mapping template variable names to Python objects.
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))
#
#     # render shortcut rather than template w/ context, httpresp etc
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)



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
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

from .models import Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
def vote(request, question_id):
    # We are using the reverse() function in the HttpResponseRedirect constructor in this example.
    # This function helps avoid having to hardcode a URL in the view function.
    # It is given the name of the view that we want to pass control to and the variable
    # portion of the URL pattern that points to that view. In this case, using the URLconf we set up
    # in Tutorial 3, this reverse() call will return a string like
    #
    # '/polls/3/results/'
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

'''
Note

The code for our vote() view does have a small problem.
 It first gets the selected_choice object from the database, then computes the new value of votes, 
 and then saves it back to the database. If two users of your website try to vote at exactly the same time, 
 this might go wrong: The same value, let’s say 42, will be retrieved for votes. Then, for both users the new 
 value of 43 is computed and saved, but 44 would be the expected value.

This is called a race condition. If you are interested, you can read
 Avoiding race conditions using F() to learn how you can solve this issue.
'''


### updaste for generic views
from django.views import generic
from django.utils import timezone
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


'''
Note that any of Django’s default admin templates can be overridden. To override a template, do the same 
thing you did with base_site.html – copy it from the default directory into your custom directory, and make changes.

'''


