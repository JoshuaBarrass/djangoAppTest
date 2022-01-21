from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
# Create your views here.


# def index(request):  # When at index, this will show
#     latestQuestionList = Question.objects.order_by('-pubDate')[:5]  #Retrieves the last 5 Questions
    
#     context = {'latestQuestionList' : latestQuestionList,       # creates json context data relevent to data needed within the html
#                }
    
#     return render(request, 'polls/index.html', context)     # returns from request with located template with the given context data

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latestQuestionList'
    
    def get_queryset(self):
        return Question.objects.order_by('-pubDate')[:5]

# def detail(request, questionId):
    
#     question = get_object_or_404(Question, pk=questionId)
    
#     return render(request, 'polls/detail.html', {'question' : question})
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def results(request, questionId):
    
#     question = get_object_or_404(Question, pk=questionId)       # gets the relevent question
    
#     context = {'question' : question        # makes it json context for render
#                }
    
#     return render(request, 'polls/results.html', context)   # returns template with json data for rendering

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# POST Request functions, can't reall be classes

def vote(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    
    try:
        selectedChoice: Choice = question.choice_set.get(pk=request.POST['choice'])
        
    except (KeyError, Choice.DoesNotExist):
        returnContext = {'question' : question, 
                        'errorMessage': "You didn't set a choice.",
                        }
        
        return render(request, 'polls/detail.html', returnContext)
    else:
        selectedChoice.votes += 1
        selectedChoice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # redirects to polls:results with the id for the valid results 
