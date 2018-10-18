from django.urls import path

from . import views

app_name='teams'


urlpatterns = [
    path('', views.TeamListView.as_view(), name='list'),
    path('<pk>/', views.TeamDetailView.as_view(), name='detail'),
]
