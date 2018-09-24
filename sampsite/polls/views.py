from django.http import HttpResponse

# Create your views here.
from .models import  Question,Choice

#render a page whenever it is passed a template
from django.shortcuts import  render

from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

from django.urls import reverse

# display 5 latest question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    #output = ','.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


# this function display questions and choices assigned to it
def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    #return HttpResponse(f"you're looking at question {question_id}")
    return render(request, 'polls/detail.html', {'question':question})

#this will display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #response = f"You're looking at the results of question {question_id}"
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',  {
            'question':question,
            'error_message':"You didn't select a choice"
        })
    else :
        selected_choice.votes +=1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results',
                                        args=(question.id,)))

