from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homePage'),
    path('form/',form_view,name='form_page'),
    path('result/',result_view,name='result_page')
]
