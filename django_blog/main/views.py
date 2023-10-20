from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from http import HTTPStatus
from random import choice as rnd_choice
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from .forms import LoginForm, RegisterForm, CommentForm, NewArticleForm
from .models import Article, Comment, Topic


def teapot(request):
    return render(request, 'main/teapot.html', status=HTTPStatus.IM_A_TEAPOT)


def show_home_page(request):
    def split_articles(articles, columns_count=1):
        columns = []
        for col_index in range(columns_count):
            column = []
            for i in range(col_index, len(articles), columns_count):
                column.append(articles[i])
            columns.append(column)
        return columns

    topic_id = request.GET.get('topic_id')
    if topic_id:
        selected_topic = Topic.objects.get(pk=topic_id)
        articles = selected_topic.articles.all()
    else:
        articles = Article.objects.all()
    topics = Topic.objects.all()
    article_columns = split_articles(articles, 3)
    return render(request,
                  'main/home_page.html',
                  {'topics': topics, 'article_columns': article_columns, 'topic_id': topic_id and int(topic_id)})


def show_about(request):
    return render(request, 'main/about.html')


def random_article(request):
    article_id = rnd_choice(Article.objects.all()).pk
    return redirect(reverse('main:article', kwargs={"article_id": article_id}))


def show_article(request, article_id):
    # article = get_object_or_404(Article, pk=article_id)
    try:
        article = Article.objects.get(pk=article_id)
        comments = reversed(article.comments.all())
        topics = article.topics.all()
        return render(request, 'main/post/article.html',
                      {'article': article, 'comments': comments, 'topics': topics, 'form': CommentForm()})
    except ObjectDoesNotExist:
        return redirect(reverse('main:teapot'))


def add_comment(request, article_id):
    if not request.method == 'POST':
        return HttpResponseRedirect('/')

    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return HttpResponseRedirect('/')

    form = CommentForm(request.POST)
    if not isinstance(request.user, User):
        form.add_error('message', "You need to log in")
    if form.is_valid():
        Comment.objects.create(article=article,
                               author=request.user,
                               message=form.cleaned_data.get('message'),
                               created=timezone.now())
    return redirect(reverse('main:article', kwargs={"article_id": article_id}))


def create_article(request):
    if request.method == 'POST':
        form = NewArticleForm(request.POST)
        if not isinstance(request.user, User):
            form.add_error('content', "You need to log in")
        if form.is_valid():
            article = Article.objects.create(author=request.user,
                                             title=form.cleaned_data.get('title'),
                                             content=form.cleaned_data.get('content'),
                                             created=timezone.now())
            return redirect(reverse('main:article', kwargs={"article_id": article.pk}))
    else:
        form = NewArticleForm()
    return render(request, 'main/post/create_article.html', {'form': form})

    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.cleaned_data.pop('password_again')
    #         User.objects.create_user(**form.cleaned_data)
    #         # login(request, user)
    #         return redirect(reverse('main:register'))
    # else:
    #     form = RegisterForm()
    # return render(request, 'main/user/register_account.html', {'form': form})


def update_article(request, article_id):
    return render(request, 'main/post/update_article.html')


def delete_article(request, article_id):
    return render(request, 'main/post/delete_article.html')


def subscribe_topic(request, topic):
    return HttpResponse(f"Subscribe to topic #{topic}")


def unsubscribe_topic(request, topic):
    return HttpResponse(f"Unsubscribe from topic #{topic}")


def show_user_profile(request, username):
    return HttpResponse(f"{username}'s profile")


def set_password(request):
    return HttpResponse("Set password")


def set_userdata(request):
    return HttpResponse("Set userdata")


def deactivate_account(request):
    return render(request, 'main/user/deactivate_account.html')


def register_account(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data.pop('password_again')
            User.objects.create_user(**form.cleaned_data)
            # login(request, user)
            return redirect(reverse('main:register'))
    else:
        form = RegisterForm()
    return render(request, 'main/user/register_account.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'main/user/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def show_archive(request, year, month):
    if 0 < int(year) <= 2023 and 0 < int(month) <= 12:
        return HttpResponse(f"Year: {int(year)}, Month: {int(month)}")
    return HttpResponseNotFound("Not Found")
