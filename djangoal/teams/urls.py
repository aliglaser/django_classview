from django.urls import path

from . import views

app_name='teams'


urlpatterns = [
    path('', views.TeamListView.as_view(), name='list'),
    path('create/', views.TeamCreateView.as_view(), name='create'),
    path('<pk>/', views.TeamDetailView.as_view(), name='detail'),
    path('edit/<pk>/', views.TeamUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.TeamDeleteView.as_view(), name='delete'),
]
