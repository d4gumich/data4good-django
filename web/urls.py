
from django.urls import path
from django.contrib import admin
from . import views
from django.views.generic import TemplateView
# from web.views import ContributeView

app_name='web'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('organization', views.OrganizationView.as_view(), name='all'),
    path('projects', views.ProjectsView.as_view(), name='projects'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('datasets', views.DataSetsView.as_view(), name='all'),
    path('contribute', views.ContributeView.as_view(), name='all'),
    path('faq', views.FAQView.as_view(), name='all'),
]