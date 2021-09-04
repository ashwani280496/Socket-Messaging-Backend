from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views
from django.conf.urls import include

from .consumers import TicTacToeConsumer
from .views import *
websocket_urlpatterns = [
    url(r'^ws/play/(?P<room_code>\w+)/$', TicTacToeConsumer.as_asgi()),
]
abc = DefaultRouter()
abc.include_root_view = False
abc.register(r'chat-groups', views.ChatGroupViewsSet)
abc.register(r'members', MembersViewSet)

urlpatterns=[
    url(r'^', include(abc.urls))
]