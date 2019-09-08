from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.


class AdviceList(generics.ListCreateAPIView):
    """
    Return a list of all the existing advices, gives ability to create a new one.
    """
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


class AdviceDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an advice.
    """
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


class QuizQuestionList(generics.ListCreateAPIView):
    """
    Return a list of all the existing quiz questions, gives ability to create a new one.
    """
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer


class QuizQuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a quiz question.
    """
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer


class UserList(generics.ListCreateAPIView):
    """
    Return a list of all the existing users, gives ability to create a new one.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserScoreDetails(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update an user score.
    """
    queryset = UserScore.objects.all()
    serializer_class = UserScoreSerializer


class ForumQuestionList(generics.ListCreateAPIView):
    """
    Return a list of all the existing forum questions, gives ability to create new one.
    """
    queryset = ForumQuestion.objects.all()
    serializer_class = ForumQuestionSerializer


class ForumQuestionDetails(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a forum question.
    """
    queryset = ForumQuestion.objects.all()
    serializer_class = ForumQuestionSerializer


class ForumAnswerList(generics.ListCreateAPIView):
    """
    Return a list of all the existing forum answers, gives ability to create new one.
    """
    queryset = ForumAnswer.objects.all()
    serializer_class = ForumAnswerSerializer


class ForumAnswerDetails(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a forum answer.
    """
    queryset = ForumAnswer.objects.all()
    serializer_class = ForumAnswerSerializer
