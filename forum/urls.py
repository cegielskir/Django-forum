from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout
from django.conf import settings


app_name = 'forum'

urlpatterns = [
    #/forum/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login/$', views.UserLoginView.as_view(), name='login'),

    url(r'^logout/$', logout, {'next_page': '/forum/'}, name='logout'),

    #errors
    url(r'^error/(?P<error>([a-zA-Z0-9 ]+))$', views.ErrorView.as_view(), name='error'),

    #/forum/title/
    url(r'^(?P<slug>([a-zA-Z0-9 ]+))/$', views.DetailView.as_view(), name='detail'),

    #/forum/topic/add/
    url(r'topic/add/$', views.TopicCreate.as_view(), name='topic-add'),

    url(r'^(?P<topic>([a-zA-Z0-9 ]+))/add-answer$', views.AnswerCreate.as_view(), name='answer-add')
]