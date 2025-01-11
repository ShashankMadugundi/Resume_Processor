from django.urls import path
from . import views
from .views import ResumeExtractView
urlpatterns = [
    path('', views.home, name='home'),
    path('api/extract_resume/', ResumeExtractView.as_view(), name='extract_resume'),
]
