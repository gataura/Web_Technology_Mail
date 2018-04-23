from django.contrib.auth.models import User
from qa.models import Question, Answer
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    limit = request.GET.get('limit', 10)
    questions = Question.objects.all().order_by('-id')
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'que_list.html',
                  {
                      'questions': page.object_list,
                      'title': 'Latest',
                      'paginator': paginator,
                      'page': page,
                  })


def popular(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    limit = request.GET.get('limit', 10)
    questions = Question.objects.all().order_by('-rating')
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'que_list.html',
                  {
                      'questions': page.object_list,
                      'title': 'Popular',
                      'paginator': paginator,
                      'page': page,
                  })


def question(request, pk):
    try:
        q = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        raise Http404
    a = Answer.objects.all()
    u = User.objects.all()
    return render(request, 'question.html',
                  {
                      'question': q,
                      'answer': a,
                      'user': u,
                   })

def qa_list_main(request):
    since = request.GET.get('since')
    quest = QaManager.objects.main(since)
    return render(request, 'que_list.html',
                  {
                      'questions':quest,
                      'since': quest[-1].id,
                  })