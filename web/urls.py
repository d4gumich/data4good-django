
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
    path('projects/cio4good', views.CIO4GoodView.as_view(), name='cio4good'),
    path('projects/pdfparsing', views.PDFParsingView.as_view(), name='pdfparsing'),
    path('projects/digitalidentification', views.DigitalIdentificationView.as_view(), name='digitalidentification'),
    path('projects/refugees', views.RefugeesView.as_view(), name='refugees'),
    path('datasets', views.DataSetsView.as_view(), name='all'),
    path('contribute', views.ContributeView.as_view(), name='all'),
    path('faq', views.FAQView.as_view(), name='all'),
]