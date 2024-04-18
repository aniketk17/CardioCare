from django.urls import path
from .views import *

urlpatterns = [
    path('',chat_bot,name="chat_bot_page"),
    path('getResponse/',get_response,name="get_response"),
]