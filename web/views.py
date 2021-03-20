from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from web.models import Task, Project

# PDF Parsing
import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import sparse


#class MainView(LoginRequiredMixin, View) :
class MainView(TemplateView) :
    def get(self, request):
        return render(request, 'web/home.html')

class ProjectsView(TemplateView) :
    template_name = "web/projects.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['project_list'] = Project.objects.all();

    #     if context['project_list'] and context['project_list'] == 'cio4good' :
    #         template_name = "web/project_cio4good.html"

    #     return context
    def get(self, request):
        return render(request, 'web/projects.html', context)

# class ProjectDetailView(TemplateView) :
#     # def get(self, request, project):
#     #     # project = request.GET.get('project', False)
#     #     if project and project == 'cio4good' :
#     #         return render(request, "web/project_cio4good.html")
#     template_name = "web/projects.html"

#     def get(self, request, pk) :
#         project = Project.objects.get(id=pk)
#         context = { 'project' : project}

#         if project.name ==  'CIO4Good':
#             return render(request, "web/project_cio4good.html")#, context)
#         if project.name ==  'PDF Parsing':
#             if request.method == 'GET':
#                 print(request.GET)
#                 return render(request, "web/project_pdfparsing.html")#, context)

#             elif request.method == 'POST':
#                 print(request.POST)
#                 return render(request, "web/project_pdfparsing.html")

#         return render(request, self.template_name, context)

class CIO4GoodView(TemplateView) :
    def get(self, request) :
        return render(request, "web/project_cio4good.html")#, context)

class ChetahView(TemplateView) :
    template_name = "web/projects.html"

    def get(self, request):
        if request.method == 'GET':
            # Debug
            print(request.GET)
            
            return render(request, "web/project_chetah.html")

    def post(self, request, **kwargs):
        if request.method == 'POST':
            # Debug
            print(request.POST)

            context = {
                'search_query': "",
                'search_results': [],
            }
            query = request.POST['search-query']
            context['search_query'] = query
            
            # Prepare dataframe
            #Uncomment in test, comment in prod
            # df_pdfs = pd.read_csv('final_with_cluster.csv')
            #Uncomment in prod, comment in test
            df_pdfs = pd.read_csv('/home/D4GUMSI/data4good-django/final_with_cluster.csv')
            
            # Extract summaries from PDFs and queries from query list
            summaries = [x for x in df_pdfs.summary]
            # queries = [x for x in df_queries.Query]

            vectorizer = TfidfVectorizer()
            class BM25(object):
                def __init__(self, b=0.75, k1=1.6):
                    self.vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
                    self.b = b
                    self.k1 = k1

                def fit(self, X):
                    """ Fit IDF to documents X """
                    self.vectorizer.fit(X)
                    y = super(TfidfVectorizer, self.vectorizer).transform(X)
                    self.avdl = y.sum(1).mean()

                def transform(self, q, X):
                    """ Calculate BM25 between query q and documents X """
                    b, k1, avdl = self.b, self.k1, self.avdl

                    # apply CountVectorizer
                    X = super(TfidfVectorizer, self.vectorizer).transform(X)
                    len_X = X.sum(1).A1
                    q, = super(TfidfVectorizer, self.vectorizer).transform([q])
                    assert sparse.isspmatrix_csr(q)

                    # convert to csc for better column slicing
                    X = X.tocsc()[:, q.indices]
                    denom = X + (k1 * (1 - b + b * len_X / avdl))[:, None]
                    idf = self.vectorizer._tfidf.idf_[None, q.indices] - 1.
                    numer = X.multiply(np.broadcast_to(idf, X.shape)) * (k1 + 1)                                                          
                    return (numer / denom).sum(1).A1

            bm25 = BM25()
            bm25.fit(summaries)
            query_sample = bm25.transform(query, summaries)

            weights = []
            for i in query_sample:
                if i > 1:
                    weights.append(i)

            sorted_top = sorted(weights, key = lambda x: x, reverse = True)[:10]

            # Debug
            print(sorted_top)

            sorted_top_i = [np.where(query_sample == i) for i in sorted_top]
            top_indexes = [x[0][0] for x in sorted_top_i]

            # Debug
            print('Query: ' + query + '\n')

            for i in top_indexes:
                # Process the clusters associated with the PDF
                clusters_list = []

                # Create a new PDF dictionary and add it to the list of search results
                pdf = {
                    "title": str(df_pdfs.Title[i]),
                    "date": df_pdfs.Date[i],
                    "link": str(df_pdfs.URL[i]),
                    "cluster": str(df_pdfs.cluster[i]),
                    "summary_short": str(df_pdfs.summary[i])[:450] + "...", # Truncate summary after 450 characters
                    "summary_full": str(df_pdfs.summary[i]),
                }
                context['search_results'].append(pdf)       
            # print(context)         

            return render(request, "web/project_chetah.html", context)


# class DataSetsView(TemplateView) :
#     def get(self, request):
#         return render(request, 'web/datasets.html')#, ctx)

# class ContributeView(TemplateView) :
#     template_name = "web/contribute.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['task_list'] = Task.objects.all()
#         return context

