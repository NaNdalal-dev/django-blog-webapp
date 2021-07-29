from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='blogurl'),
    path('/<str:link>',blog_in_detail,name='blog_in_detail')
]