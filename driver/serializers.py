from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class AdviceSerializer(serializers.HyperlinkedModelSerializer):
    quiz_questions = serializers.PrimaryKeyRelatedField(many=True, queryset=QuizQuestion.objects.all())

    class Meta:
        model = Advice
        fields = ('id', 'title', 'content', 'image', 'video', 'quiz_questions')


class QuizQuestionSerializer(serializers.HyperlinkedModelSerializer):
    advice = serializers.PrimaryKeyRelatedField(queryset=Advice.objects.all())

    class Meta:
        model = QuizQuestion
        fields = ('advice', 'content', 'false_answer_1', 'false_answer_2', 'true_answer')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_score = serializers.SlugRelatedField(slug_field='points', read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'user_score')


class UserScoreSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = UserScore
        fields = ('user', 'points')


class ForumQuestionSerializer(serializers.HyperlinkedModelSerializer):
    question_user = serializers.CharField(source='question_user.username')
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ForumQuestion
        fields = ('question_user', 'question_title', 'question_content', 'answer_user', 'answers')


class ForumAnswerSerializer(serializers.HyperlinkedModelSerializer):
    answer_user = serializers.CharField(source='answer_user.username')
    forum_question_id = serializers.PrimaryKeyRelatedField(queryset=ForumQuestion.objects.all())

    class Meta:
        model = ForumAnswer
        fields = ('answer_user', 'forum_question_id', 'answer_content')