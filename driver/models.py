from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserScore(models.Model):
    user = models.OneToOneField(User, related_name='user_score', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)


class ForumQuestion(models.Model):
    question_user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=256, null=True)
    question_content = models.TextField()

    def __str__(self):
        return self.question_title


class ForumAnswer(models.Model):
    answer_user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    forum_question_id = models.ForeignKey(ForumQuestion, related_name='answers', on_delete=models.CASCADE)
    answer_content = models.TextField()


class Advice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='', default='No image')
    video = models.FileField(upload_to='media/', null=True, blank=True, verbose_name='', default='No video')

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    advice = models.ForeignKey(Advice, related_name='quiz_questions', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    false_answer_1 = models.CharField(max_length=256)
    false_answer_2 = models.CharField(max_length=256)
    true_answer = models.CharField(max_length=256)
