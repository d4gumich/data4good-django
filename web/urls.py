import os
from django.urls import path
from django.contrib import admin
from django.views.static import serve
from . import views
from django.views.generic import TemplateView
# from web.views import ContributeView

app_name='web'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('projects/cio4good', views.CIO4GoodView.as_view(), name='cio4good'),
    path('projects/chetah', views.ChetahView.as_view(), name='chetah'),
    path('projects/simex', views.SimexView.as_view(), name='simex'),
    path('projects/hangul', views.HangulView.as_view(), name='hangul')
]

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# urlpatterns += [
#     path('favicon.ico', serve, {
#         'path': 'favicon.ico',
#         'document_root': os.path.join(BASE_DIR, 'static/images'),
#         }
#     ),
# ]