from django.contrib import admin
from core.models import MyUser, Post


admin.site.register(MyUser)
admin.site.register(Post)