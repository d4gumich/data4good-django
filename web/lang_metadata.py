#creating dataframe with columns for each metadata- (Title, Date)and Content, assigning ID to each PDF and its text extraction.
def df_pdfs(meta, keywords):
  unique_id = []
  title_list = []
  date_list = []
  language_list = []
  content_list = keywords

  count=0
  for d in metadata:
    if 'title' in d:
       title_list.append(d['title'])
    else:
      title_list.append(file_name[count][:-4]) #remove the '.pdf from file name'
    count+=1
  
  # [title_list.append(d['title']) if 'title' in d else title_list.append('null') for d in meta]
  [date_list.append(d['date']) if 'date' in d else date_list.append('null') for d in meta]
  [language_list.append(d['language']) if 'language' in d else language_list.append('null') for d in meta]
  counter = 0
  for i in meta:
    unique_id.append(counter)
    counter += 1
  
  df = pd.DataFrame()
  df['ID'] = unique_id
  df['Title'] = title_list
  df['Date'] = date_list
  df['Content'] = content_list
  df['Language'] = language_list
  df['file_path'] = item_list


  return df


 import spacy
from spacy_langdetect import LanguageDetector
nlp = spacy.load("en_core_web_md")
nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
nlp.max_length = 1500000
df_lang['lang'] = df_lang['Content'].apply(lambda x: nlp(x)._.language)
df_lang['lang1'] = df_lang.lang.apply(lambda x: x.get('language'))
final_df = df_lang[df_lang["lang1"] == 'en']

