"""
ASGI config for healthguru project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
# from decouple import config
from django.core.asgi import get_asgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "healthguru.settings")

django_asgi_app = get_asgi_application()
import chatbot.routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # We will add WebSocket protocol later. For now, it's just HTTP.
        # "websocket": AllowedHostsOriginValidator(
        #     AuthMiddlewareStack(URLRouter(chatbot.routing.websocket_urlpatterns))
        # ),
    }
)