from users.views import test_page
from django.urls import path
from django.urls import re_path
from . import consumers

urlpatterns = [
    path('', test_page)
]


websocket_urlpatterns = [
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
]

