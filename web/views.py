from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from web.models import Task, Project
# from website.forms import MakeForm

# Create your views here.

#class MainView(LoginRequiredMixin, View) :
class MainView(TemplateView) :
    def get(self, request):
        return render(request, 'web/home.html')#, ctx)

class ProjectsView(TemplateView) :
    template_name = "web/projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.all();

        if context['project_list'] and context['project_list'] == 'cio4good' :
            template_name = "web/project_cio4good.html"

        return context

class ProjectDetailView(TemplateView) :
    # def get(self, request, project):
    #     # project = request.GET.get('project', False)
    #     if project and project == 'cio4good' :
    #         return render(request, "web/project_cio4good.html")
    template_name = "web/projects.html"

    def get(self, request, pk) :
        project = Project.objects.get(id=pk)
        context = { 'project' : project}

        if project.name ==  'CIO4Good':
            return render(request, "web/project_cio4good.html")#, context)

        return render(request, self.template_name, context)

class DataSetsView(TemplateView) :
    def get(self, request):
        return render(request, 'web/datasets.html')#, ctx)

class ContributeView(TemplateView) :
    template_name = "web/contribute.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = Task.objects.all();
        return context

class OrganizationView(TemplateView) :
    def get(self, request):
        return render(request, 'web/organization.html')#, ctx)

class FAQView(TemplateView) :
    def get(self, request):
        return render(request, 'web/faq.html')#, ctx)