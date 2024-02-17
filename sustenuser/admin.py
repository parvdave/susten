from django.contrib import admin
from .models import TreeHacksUser, Score, Message, MessageIntent

# Register your models here.
admin.site.register(TreeHacksUser)
admin.site.register(Score)
admin.site.register(Message)
admin.site.register(MessageIntent)
