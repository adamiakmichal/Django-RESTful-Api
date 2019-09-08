"""Portfolio_Project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls
from driver import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advices/', views.AdviceList.as_view()),
    path('advices/<int:pk>/', views.AdviceDetails.as_view()),
    path('quiz_questions/', views.QuizQuestionList.as_view()),
    path('quiz_questions/<int:pk>/', views.QuizQuestionDetails.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('user_score/<int:pk>/', views.UserScoreDetails.as_view()),
    path('forum_questions/', views.ForumQuestionList.as_view()),
    path('forum_questions/<int:pk>/', views.ForumQuestionDetails.as_view()),
    path('forum_answers/', views.ForumAnswerList.as_view()),
    path('forum_answers/<int:pk>/', views.ForumAnswerDetails.as_view()),
    path('docs/', include_docs_urls(title='driver', public=False)),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
