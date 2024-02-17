from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:id>/scores',views.get_scores,name="get-scores-view"),
    path('user/<str:user_id>/messages/',views.message_action,name="message-action"),
    path('admin/', admin.site.urls),
]
