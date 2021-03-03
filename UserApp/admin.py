from django.contrib import admin
from .models import FeedBack
from django.contrib.auth.models import Group


admin.site.register(FeedBack)
admin.site.unregister(Group)