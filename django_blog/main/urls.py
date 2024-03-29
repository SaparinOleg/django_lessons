from django.urls import path, re_path
from .views import (
    add_comment,
    random_article,
    create_article,
    show_home_page,
    show_about,
    set_password,
    deactivate_account,
    register_account,
    login,
    logout,
    subscribe_topic,
    unsubscribe_topic,
    show_user_profile,
    show_article,
    update_article,
    delete_article,
    show_archive,
    teapot,
    )

app_name = 'main'

urlpatterns = [
    path('', show_home_page, name='home_page'),
    path('about/', show_about, name='about'),
    path('set-password/', set_password, name='set_password'),
    path('deactivate/', deactivate_account, name='deactivate_account'),
    path('register/', register_account, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('create/', create_article, name='create_article'),
    path('topics/<int:topic_id>/subscribe/', subscribe_topic, name='subscribe'),
    path('topics/<int:topic_id>/unsubscribe/', unsubscribe_topic, name='unsubscribe'),
    path('profile/<str:username>/', show_user_profile, name='username'),
    path('random-article/', random_article, name='random_article'),
    path('article/<int:article_id>/', show_article, name='article'),
    path('<int:article_id>/comment/', add_comment, name='add_comment'),
    path('<int:article_id>/update/', update_article, name='update'),
    path('<int:article_id>/delete/', delete_article, name='delete'),
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', show_archive, name='archive'),
    re_path(r'^.*/$', teapot, name='teapot'),
]
