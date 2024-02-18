from django.contrib import admin
from .models import TreeHacksUser, Score, Message,Store,Item

# Register your models here.
admin.site.register(TreeHacksUser)
admin.site.register(Score)
admin.site.register(Message)
admin.site.register(Store)
admin.site.register(Item)
