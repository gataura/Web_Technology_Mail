from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(default='', max_length=255)
    text = models.TextField(default='')
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='question_user')
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def __str__(self):
        return self.title

    def build_url(self):
        return '/question/{}/'.format(self.id)


class Answer(models.Model):
    text = models.TextField(default='')
    added_at = models.DateField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, related_name='answer_question')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='answer_user')

    def __str__(self):
        return self.text

#class QaManager(models.Manager):
  #  def main(self, since, limit = 10):
    #    qs = self.order_by('-id')
     #   res = []
     #   if since is not None:
      #      qs = qs.filter(id__lt=since)
       # for p in qs[:100]:
        #    if len(res) == 0:
        #        res.append(p)
        #    if len(res) >= limit:
       #         break
       # return res
