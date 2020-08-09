from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from . import views

#Forbinder views til urls
urlpatterns = [
    path('users/', views.UserViewAll.as_view()),
    path('usersCreate/', views.UserCreate.as_view()),
    path('users/<int:pk>', views.UserViewSpecific.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
