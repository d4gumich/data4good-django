
from django.shortcuts import render
from django.views.generic import TemplateView
import os
import json
import time

#import custom modules here
from .chetah_v1 import search
from .hangul import run_hangul

class MainView(TemplateView):
    def get(self, request):
        return render(request, 'web/home.html')


class CIO4GoodView(TemplateView):
    def get(self, request):
        return render(request, "web/project_cio4good.html")  # , context)


class SimexView(TemplateView):
    def get(self, request):
        return render(request, "web/project_simex.html")  # , context)


class ChetahView(TemplateView):
    template_name = "web/projects.html"

    def get(self, request):
        if request.method == 'GET':
            return render(request, "web/project_chetah.html")

    def post(self, request):
        if request.method == 'POST':
            start_time=time.time()
            query = request.POST['search-query']
            context = {
                'search_query': query,
                'search_results': search(query),
                'search_time': round(time.time()-start_time,3)
            }
            return render(request, "web/project_chetah.html", context)

class HangulView(TemplateView):
    template_name = "web/project_hangul.html"

    def get(self, request):
        if request.method == 'GET':
            return render(request, "web/project_hangul.html")
    
    def post(self, request):
        if request.method == 'POST':
           temp_path = request.FILES['uploaded_pdf'].temporary_file_path()
           file_name = request.FILES['uploaded_pdf'].name
           meta_content = run_hangul(temp_path)
           meta_content['file_name'] = file_name
           os.remove(temp_path)
           return render(request, "web/project_hangul.html", { 'meta_content': json.dumps(meta_content, indent=2)})
    
