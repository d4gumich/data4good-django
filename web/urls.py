
from django.urls import path
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
    # path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
    # path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
    # path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
    # path('lookup/', views.MakeView.as_view(), name='make_list'),
    # path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    # path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    # path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
]