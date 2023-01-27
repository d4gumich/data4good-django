from django.shortcuts import render
from django.views.generic import TemplateView
import os
import json
from .hangul import init,run_hangul
=======
>>>>>>> refs/remotes/origin/hangul

from django.shortcuts import render
from django.views.generic import TemplateView
import os
import json
import time

#import custom modules here
from .chetah_v1 import search
from .hangul import run_hangul

<<<<<<< HEAD
# class MainView(LoginRequiredMixin, View) :
=======
>>>>>>> refs/remotes/origin/hangul
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
        init()
        if request.method == 'GET':
<<<<<<< HEAD
            # Debug
            # print(request.GET)

=======
>>>>>>> refs/remotes/origin/hangul
            return render(request, "web/project_chetah.html")

    def post(self, request):
        if request.method == 'POST':
<<<<<<< HEAD
            # Debug
            # print(request.POST)

=======
            start_time=time.time()
            query = request.POST['search-query']
>>>>>>> refs/remotes/origin/hangul
            context = {
                'search_query': query,
                'search_results': search(query),
                'search_time': int(round(time.time()-start_time,3)*1000)
            }
<<<<<<< HEAD
            query = request.POST['search-query']
            context['search_query'] = query

            # Prepare dataframe
            #Uncomment in test, comment in prod
            # df_pdfs = pd.read_csv('final_with_cluster.csv')
            #Uncomment in prod, comment in test
            df_pdfs = pd.read_csv(
                '/home/D4GUMSI/data4good-django/final_with_cluster.csv')

            # Extract summaries from PDFs and queries from query list
            summaries = [x for x in df_pdfs.summary]
            # queries = [x for x in df_queries.Query]

            class BM25(object):
                def __init__(self, b=0.75, k1=1.6):
                    self.vectorizer = TfidfVectorizer(
                        norm=None, smooth_idf=False)
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
                    numer = X.multiply(
                        np.broadcast_to(idf, X.shape)) * (k1 + 1)
                    return (numer / denom).sum(1).A1

            bm25 = BM25()
            bm25.fit(summaries)
            query_sample = bm25.transform(query, summaries)

            weights = []
            for i in query_sample:
                if i > 1:
                    weights.append(i)

            sorted_top = sorted(weights, key=lambda x: x, reverse=True)[:10]

            # Debug
            # print(sorted_top)

            sorted_top_i = [np.where(query_sample == i) for i in sorted_top]
            top_indexes = [x[0][0] for x in sorted_top_i]

            # Debug
            #print('Query: ' + query + '\n')

            for i in top_indexes:
                # Process the clusters associated with the PDF

                # Create a new PDF dictionary and add it to the list of search results
                pdf = {
                    "title": str(df_pdfs.Title[i]),
                    "date": df_pdfs.Date[i],
                    "link": str(df_pdfs.URL[i]),
                    "cluster": str(df_pdfs.cluster[i]),
                    # Truncate summary after 450 characters
                    "summary_short": str(df_pdfs.summary[i])[:450] + "...",
                    "summary_full": str(df_pdfs.summary[i]),
                }
                context['search_results'].append(pdf)
            # print(context)

=======
>>>>>>> refs/remotes/origin/hangul
            return render(request, "web/project_chetah.html", context)

class HangulView(TemplateView):
    template_name = "web/project_hangul.html"

<<<<<<< HEAD
# class DataSetsView(TemplateView) :
#     def get(self, request):
#         return render(request, 'web/datasets.html')#, ctx)

# class ContributeView(TemplateView) :
#     template_name = "web/contribute.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['task_list'] = Task.objects.all()
#         return context

class HangulView(TemplateView):
    template_name = "web/project_hangul.html"

=======
>>>>>>> refs/remotes/origin/hangul
    def get(self, request):
        if request.method == 'GET':
            return render(request, "web/project_hangul.html")
    
    def post(self, request):
        if request.method == 'POST':
<<<<<<< HEAD
           temp_path = request.FILES['uploaded_pdf'].temporary_file_path()
           meta_content = json.dumps(run_hangul(temp_path), indent=2)
           os.remove(temp_path)
           return render(request, "web/project_hangul.html", { 'meta_content': meta_content})
=======
           start_time=time.time()
           temp_path = request.FILES['uploaded_pdf'].temporary_file_path()
           file_name = request.FILES['uploaded_pdf'].name
           meta_content = run_hangul(temp_path)
           context = {
               'meta_content': json.dumps(meta_content, indent=2),
               'locations':', '.join([location[0][0] for location in meta_content['locations']]) if meta_content['locations'] else None,
               'disasters':', '.join([disaster for disaster in meta_content['disasters']]) if meta_content['disasters'] else None,
               'file_name': file_name,
               'pages': meta_content['metadata'][0]['metadata']['No.of Pages'],
               'hangul_time': f'{int(round(time.time()-start_time,3)*1000)} ms'
           }
           os.remove(temp_path)
           return render(request, "web/project_hangul.html", context)
>>>>>>> refs/remotes/origin/hangul
    
