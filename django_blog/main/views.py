from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from http import HTTPStatus
from random import choice as rnd_choice
from django.core.exceptions import ObjectDoesNotExist

from .models import Article, Comment, Topic


def teapot(request):
    return render(request, 'main/teapot.html', status=HTTPStatus.IM_A_TEAPOT)


def show_home_page(request):
    topic_id = request.GET.get('topic_id')
    if topic_id:
        topics = Topic.objects.filter(pk=topic_id)
        articles = topics.first().articles.all()
    else:
        topics = Topic.objects.all()
        articles = Article.objects.all()
    return render(request,
                  'main/home_page.html',
                  {'articles': articles, 'topics': topics})


def show_about(request):
    return render(request, 'main/about.html')


def random_article(request):
    article_id = rnd_choice(Article.objects.all()).pk
    return redirect(reverse('main:article', kwargs={"article_id": article_id}))


def show_article(request, article_id):
    # article = get_object_or_404(Article, pk=article_id)
    try:
        article = Article.objects.get(pk=article_id)
        comments = article.comments.all()
        topics = article.topics.all()
        return render(request,
                      'main/post/article.html',
                      {'article': article, 'comments': comments, 'topics': topics})
    except ObjectDoesNotExist:
        return redirect(reverse('main:teapot'))


def add_comment(request, article_id):
    return render(request, 'main/post/add_comment.html')


def create_article(request):
    return render(request, 'main/post/create_article.html')


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
    return render(request, 'main/user/register_account.html')


def login(request):
    return render(request, 'main/user/login.html')


def logout(request):
    return render(request, 'main/user/logout.html')


def show_archive(request, year, month):
    if 0 < int(year) <= 2023 and 0 < int(month) <= 12:
        return HttpResponse(f"Year: {int(year)}, Month: {int(month)}")
    return HttpResponseNotFound("Not Found")
