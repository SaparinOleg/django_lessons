from random import randint
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


def show_home_page(request):
    return render(request, 'main/home_page.html')


def show_about(request):
    return render(request, 'main/about.html')


def article(request):
    article_id = randint(1, 100)
    return redirect(f'/article/{article_id}')


def show_article(request, article_id):
    return render(request, 'main/post/article.html', {"id": article_id})


def add_comment(request, article_id):
    return render(request, 'main/post/add_comment.html')


def create_article(request):
    return render(request, 'main/post/create_article.html')


def update_article(request, article_id):
    return render(request, 'main/post/update_article.html')


def delete_article(request, article_id):
    return render(request, 'main/post/delete_article.html')


def show_topics(request):
    return render(request, 'main/topic/topic_list.html')


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
