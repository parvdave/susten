from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.user_login, name="login-view"),
    path('/api/scores/',views.get_scores,name="get-scores-view"),
    path('/api/scores',views.get_scores,name="get-scores-view"),
    path('user/<str:user_id>/messages/',views.message_action,name="message-action"),
    path('user/<str:user_id>/messages',views.message_action,name="message-action"),
    path('stores/',views.get_stores,name="get-stores-view"),
    path('user/<str:user_id>/stores/<str:store_id>',views.get_store,name="get-store-view"),
    path('user/<str:user_id>/stores/<str:store_id>/sell',views.sell_to_store,name="sell-to-store-view"),
    path('user/<str:user_id>/stores/<str:store_id>/item/<str:item_id>/buy',views.sell_to_store,name="sell-to-store-view"),
    path('user/<str:user_id>/stores/<str:store_id>/',views.get_store,name="get-store-view"),
    path('chat/', views.chat, name="chat-view"),
    path('admin/', admin.site.urls),
    path('progress/', views.progress, name='progress-view')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)