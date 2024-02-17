from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:id>/scores',views.get_scores,name="get-scores-view"),
    path('admin/', admin.site.urls),
]
