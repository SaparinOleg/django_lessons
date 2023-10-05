from django.http import HttpResponse


def show_home_page(request):
    return HttpResponse("Home page")


def show_about(request):
    return HttpResponse("Simple text")


def show_article(request, article):
    return HttpResponse("Article")


def add_comment(request, article):
    return HttpResponse("Comment")


def create_article(request):
    return HttpResponse("Create")


def update_article(request, article):
    return HttpResponse("Update")


def delete_article(request, article):
    return HttpResponse("Delete")


def show_topics(request):
    return HttpResponse("Topics")


def subscribe_topic(request, topic):
    return HttpResponse("Subscribe")


def unsubscribe_topic(request, topic):
    return HttpResponse("Unsubscribe")


def user_profile(request, username):
    return HttpResponse("User profile")


def set_password(request):
    return HttpResponse("Set password")


def set_userdata(request):
    return HttpResponse("Set userdata")


def deactivate_account(request):
    return HttpResponse("Deactivate account")


def register_account(request):
    return HttpResponse("Register account")


def login(request):
    return HttpResponse("Login")


def logout(request):
    return HttpResponse("Logout")
