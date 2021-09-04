from django.conf.urls import url

from chat.consumers import TicTacToeConsumer

websocket_urlpatterns = [
    url(r'^ws/play/(?P<room_code>\w+)/$', TicTacToeConsumer.as_asgi()),
]
# abc = DefaultRouter()
# abc.register(r'chat-groups',views.ChatGroupViewsSet)
# rest_urlpatterns=[
#     url(r'^',include(abc.urls))
# ]
