

from django.urls import path, include
from rest_framework import routers

from apps.fileUpload import views


urlpatterns = [
    path('image/', views.FileUploadView.as_view()),   
]