from django.http import Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.views import generic
from .models import Topic, Answer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserRegistrationForm, UserLoginForm, AnswerAddForm, TopicAddForm
from datetime import datetime


class IndexView(generic.ListView):
    template_name = 'forum/index.html'
    context_object_name = 'all_topics'

    def get_queryset(self):
        return Topic.objects.all()


class DetailView(generic.DeleteView):
    model = Topic
    slug_field = 'title'
    slug_url_kwarg = 'slug'
    template_name = 'forum/detail.html'

    def get_queryset(self):
        title = self.kwargs['slug']
        t = Topic.objects.get(title=title)
        t.visits_no += 1
        t.save()
        return Topic.objects.filter(title=title)


class TopicCreate(View):
    template_name = 'forum/topic_form.html'
    model = Topic
    form_class = TopicAddForm
    fields = ['author', 'title', 'text']


    # display blank form
    def get(self, request):
        if request.user.is_authenticated:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('forum:login')

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            # clean (normalized) data

            author = User.objects.get(username=self.request.user.username)
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            top = Topic.objects.filter(title=title)
            print(top)
            if len(top) == 1:
                raise Http404("Temat o takim tytule już istenieje")

            t = Topic(author=author, title=title, text=text)
            t.save()

            # returns User objects if credentials are correct
            return redirect(reverse('forum:detail', kwargs={'slug': title}))

        return render(request, self.template_name, {'form': form})


class AnswerCreate(View):
    model = Answer
    fields = ['author', 'text']
    form_class = AnswerAddForm
    template_name = 'forum/answer_form.html'

    # display blank form
    def get(self, request, topic):
        if request.user.is_authenticated:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('forum:login')

    # process form data
    def post(self, request, topic):
        form = self.form_class(request.POST)

        if form.is_valid():

            # clean (normalized) data

            author = User.objects.get(username=self.request.user.username)
            print(author.username)
            text = form.cleaned_data['text']
            a = Answer(author=author, text=text)
            a.save()
            t = Topic.objects.get(title=topic)
            t.answers_no += 1
            t.visits_no -= 1
            t.last_answer_date = datetime.now()
            t.last_answer_author = str(author)
            t.answers.add(a)
            t.save()

            # returns User objects if credentials are correct
            return redirect(reverse('forum:detail', kwargs={'slug': topic}))

        return render(request, self.template_name, {'form': form})


class UserFormView(View):
    form_class = UserRegistrationForm
    template_name = 'forum/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #clean (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('forum:index')

        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'forum/login_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # clean (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('forum:index')

        return render(request, self.template_name, {'form': form})