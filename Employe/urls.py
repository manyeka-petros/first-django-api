from django.urls import path
from.views import Employ,CreateEmpo

urlpatterns = [
    path('',Employ.as_view()),
    path('post/',CreateEmpo.as_view())
]
