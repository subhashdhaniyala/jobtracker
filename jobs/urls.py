from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job-list'),

    # API endpoints
    path('api/jobs/', views.JobListCreateAPI.as_view(), name='api-job-list'),
    path('api/jobs/<int:pk>/', views.JobDetailAPI.as_view(), name='api-job-detail'),
]