from django.contrib import admin
from .models import UserProfile, ChatHistory

admin.site.register(UserProfile)
admin.site.register(ChatHistory)
