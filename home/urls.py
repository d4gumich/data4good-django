from django.urls import path
from django.views.generic import TemplateView
from django.views.static import serve
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app_name='home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
]