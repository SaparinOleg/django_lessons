from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', show_home_page),
    path('about/', show_about),
    path('set-password/', set_password),
    path('deactivate/', deactivate_account),
    path('register/', register_account),
    path('login/', login),
    path('logout/', logout),
    path('create/', create_article),
    path('topics/', show_topics),
    path('topics/<int:topic>/subscribe/', subscribe_topic),
    path('topics/<int:topic>/unsubscribe/', unsubscribe_topic),
    path('profile/<str:username>/', show_user_profile),
    path('<int:article>/', show_article),
    path('<int:article>/comment/', add_comment),
    path('<int:article>/update/', update_article),
    path('<int:article>/delete/', delete_article),
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/', show_archive)
]
