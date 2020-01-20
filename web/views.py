from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

# from website.models import Auto, Make
# from website.forms import MakeForm

# Create your views here.

#class MainView(LoginRequiredMixin, View) :
class MainView(TemplateView) :
    def get(self, request):
        # mc = Make.objects.all().count();
        # al = Auto.objects.all();

        # ctx = { 'make_count': mc, 'auto_list': al }
        return render(request, 'web/home.html')#, ctx)

class ServicesView(TemplateView) :
    def get(self, request):
        # mc = Make.objects.all().count();
        # al = Auto.objects.all();

        # ctx = { 'make_count': mc, 'auto_list': al }
        return render(request, 'web/services.html')#, ctx)

class ArticlesView(TemplateView) :
    def get(self, request):
        # mc = Make.objects.all().count();
        # al = Auto.objects.all();

        # ctx = { 'make_count': mc, 'auto_list': al }
        return render(request, 'web/articles.html')#, ctx)

class CompanyView(TemplateView) :
    def get(self, request):
        # mc = Make.objects.all().count();
        # al = Auto.objects.all();

        # ctx = { 'make_count': mc, 'auto_list': al }
        return render(request, 'web/company.html')#, ctx)

class FAQView(TemplateView) :
    def get(self, request):
        # mc = Make.objects.all().count();
        # al = Auto.objects.all();

        # ctx = { 'make_count': mc, 'auto_list': al }
        return render(request, 'web/faq.html')#, ctx)