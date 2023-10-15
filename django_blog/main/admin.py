from django.contrib import admin
from .models import Article, Comment, Topic, Preference

admin.site.register(Article)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Preference)
