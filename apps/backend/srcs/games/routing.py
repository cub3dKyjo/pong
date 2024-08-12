from django.urls import re_path

from . import gameConsumer, gameQueueConsumer

websocket_urlpatterns = [
    re_path(r"^ws/rankgames/(?P<type>[\w-]+)/$", gameQueueConsumer.RankGameRoomConsumer.as_asgi()),
    re_path(r"^ws/games/start/(?P<game_id>[a-fA-F0-9\-]{36})/(?P<type>[\w-]+)/$", gameConsumer.GameConsumer.as_asgi()),
]
