from keybert import KeyBERT

kw_model = KeyBERT(model='all-mpnet-base-v2')


def generate_keywords(summary:str, top_n:int=5)->list:
    keywords = kw_model.extract_keywords(summary,
                                         stop_words='english',
                                         keyphrase_ngram_range=(1,2),
                                         highlight=False,
                                         top_n=top_n,
                                         use_maxsum=True)
    return list(dict(keywords).keys())