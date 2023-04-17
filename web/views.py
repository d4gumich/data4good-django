from django.shortcuts import render
from django.views.generic import TemplateView
import os
import json
import time

#import custom modules here
from .chetah_v1 import search
from .hangul import run_hangul
from .keyword_detection import generate_keywords

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
            results = search(query)
            context = {
                'search_query': query,
                'search_results': results,
                'search_time': int(round(time.time()-start_time,3)*1000),
                'result_size': len(results)
            }
            return render(request, "web/project_chetah.html", context)

class HangulView(TemplateView):
    template_name = "web/project_hangul.html"

    def get(self, request):
        if request.method == 'GET':
            return render(request, "web/project_hangul.html")
    
    def post(self, request):
        if request.method == 'POST':
           start_time=time.time()
           temp_path = request.FILES['uploaded_pdf'].temporary_file_path()
           file_name = request.FILES['uploaded_pdf'].name
           kp = request.POST.get('keyphrase_num', 5)
           meta_content = run_hangul(temp_path)
           meta_content['keywords'] = generate_keywords(meta_content['full_content'], int(kp))
           meta_content.pop('full_content')
           context = {
               'meta_content': json.dumps(meta_content, indent=2),
               'locations':' | '.join([location for location in meta_content['locations']]) if meta_content['locations'] else None,
               'disasters':', '.join([disaster for disaster in meta_content['disasters']]) if meta_content['disasters'] else None,
               'file_name': file_name,
               'pages': meta_content['metadata']['No.of Pages'],
               'keywords': ',\n'.join(meta_content['keywords']),
               'author': meta_content['metadata']['Author'],
               'doc_type': meta_content['metadata']['doc_type'],
               'doc_created_date': meta_content['metadata']['doc_created_date'],
               'doc_saved_date': meta_content['metadata']['doc_saved_date'],
               'doc_modified_date': meta_content['metadata']['doc_modified_date'],
               'doc_title': meta_content['metadata']['doc_title'],
               'report_type': meta_content['report_type'],
               'language': f"{meta_content['document_language']['language']} (Score: {round(meta_content['document_language']['score'], 3)})",
               'hangul_time': f'{round(time.time()-start_time, 3)} seconds'
           }
           return render(request, "web/project_hangul.html", context)
