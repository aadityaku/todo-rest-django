
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
urlpatterns = [
    path("home/",todolist,name="home"),
    path('home/<int:pk>/',todolistDetails,name="detail"),
    path('create/',createTodo,name="create"),
    path('login/',MyObtainTokenPairView.as_view(),name="token"),
    path('login/refresh',TokenRefreshView.as_view(),name="token"),
    path("register/",RegisterView.as_view(),name="register"),
    path('create/<int:id>/',updateView,name="update"),
    path('delete/<int:id>/',deleteTodo,name="delete")
]

url_patterns=format_suffix_patterns(urlpatterns)