from django.urls import path

from . import views

app_name='teams'


urlpatterns = [
    path('', views.team_list, name='list'),
    path('<pk>/', views.team_detail, name='detail'),
]