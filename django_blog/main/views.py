from django.http import HttpResponse, HttpResponseNotFound


def show_home_page(request):
    return HttpResponse("Home page")


def show_about(request):
    return HttpResponse("Simple text")


def show_article(request, article):
    return HttpResponse(f"Article #{article}")


def add_comment(request, article):
    return HttpResponse(f"Add comment to article #{article}")


def create_article(request):
    return HttpResponse("Create article")


def update_article(request, article):
    return HttpResponse(f"Update article #{article}")


def delete_article(request, article):
    return HttpResponse(f"Delete article #{article}")


def show_topics(request):
    return HttpResponse("Topics")


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
    return HttpResponse("Deactivate account")


def register_account(request):
    return HttpResponse("Register account")


def login(request):
    return HttpResponse("Login")


def logout(request):
    return HttpResponse("Logout")


def show_archive(request, year, month):
    if 0 < int(year) <= 2023 and 0 < int(month) <= 12:
        return HttpResponse(f"Year: {int(year)}, Month: {int(month)}")
    # return HttpResponse("Incorrect date")
    return HttpResponseNotFound("Not Found")
