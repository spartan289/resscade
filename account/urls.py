from django.urls import path, include
from . import views
urlpatterns = [
    path('profile/<str:username>', views.profile, name='profile'),

    path('post', views.post, name='post'),
    path('disp', views.after_logged, name='disp'),
    path('login', views.login, name='login'),
]
