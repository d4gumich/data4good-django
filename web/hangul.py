#@author- SIdra Effendi
import tika
from tika import parser
import spacy
from .disaster_detection import get_disasters
from collections import Counter
from .get_file_metadata import extract_metadata
from .location_detection import detected_potential_countries
from .report_type import detect_report_type
import re
import html2text
from spacy_langdetect import LanguageDetector
from spacy.language import Language

nlp = spacy.load('en_core_web_sm')

# def extract_pdf_content(pdf_path, content_as_pages):

#     if content_as_pages:
#         raw_xml = parser.from_file(pdf_path, xmlContent=True)
#         body = raw_xml['content'].split('<body>')[1].split('</body>')[0]
#         body_without_tag = body.replace("<p>", "").replace("</p>", "\n").replace("<div>", "").replace("</div>","\n").replace("<p />","\n")
#         text_pages = body_without_tag.split("""<div class="page">""")[1:]
#         num_pages = len(text_pages)
#         print(num_pages)
#         if num_pages==int(raw_xml['metadata']['xmpTPg:NPages']) : 
#             for i in range(3):
#             # for i in range(num_pages):
#                 print('page number: '+ str(i+1))
#                 print(text_pages[i].replace("\n", ""))
#                 print('\n')
#         pdf_content = body_without_tag
#     else:
#         parsed_pdf = parser.from_file(pdf_path)
#         pdf_content= parsed_pdf["content"].replace("\n", "")
#     return pdf_content

def get_content_pages(pdf_path):
    raw_xml = parser.from_file(pdf_path, xmlContent=True)
    body = raw_xml['content'].split('<body>')[1].split('</body>')[0]
    body_without_tag = body.replace("<p>", "").replace("</p>", "\n").replace("<div>", "").replace("</div>","\n").replace("<p />","\n")
    text_pages = body_without_tag.split("""<div class="page">""")[1:]
    num_pages = len(text_pages)
    pages_content=[]
    if num_pages==int(raw_xml['metadata']['xmpTPg:NPages']) : 
        # for i in range(5):
        for i in range(num_pages):
    #         # print('page number: '+ str(i+1))
            h = html2text.HTML2Text()
            h.ignore_links = True
            # h.escape_all = True
            text_pages[i]= h.handle(text_pages[i].replace("\n", " "))
            text_pages[i] = re.sub(r'\s*(?:https?://)?www\.\S*\.[A-Za-z]{2,5}\s*', ' ', text_pages[i].replace("\n", " ")).strip()
            pages_content.append(text_pages[i])
        pdf_content = pages_content
    return pdf_content


def get_doc_title(first_three_pages, metadata):

    char_per_page_list = list(map(int, metadata['charsPerPage'][:3]))
    mi = min(char_per_page_list)
    indexes = [index for index in range(len(char_per_page_list)) if char_per_page_list[index] == mi]

    return first_three_pages[indexes[0]]

def get_doc_summary(first_six_pages):
    # char_per_page_list = list(map(int, metadata['charsPerPage'][:6]))
    check_str = 'summary'
    summary = 'N/A'
    for page_content in first_six_pages:
        if check_str in page_content.lower():
            summary=  page_content
    return summary



def clean_doc_content(content):
    return content.replace("\n", "")


def extract_pdf_data(file_paths, want_metadata=True, want_content=False):
    '''Given a list of path to PDFs, iterate over the list,
     and for each string, read in the PDF form its path and 
     return extracted text.

     The flags might be changed during further development. 
     Right now they are designed to help in the process of 
     development and debugging.
     Developing what details about the document we want to 
     look at closely - metadata or content or both.
     It also returns content as pages so that we can decide 
     which pages to target going forward for information.

     @type list_of_path_to_pdf: list of string - [str1, str2]
     @param list_of_path_to_pdf: path of the pdf file to be read
     @type want_metadata: boolean
     @param want_metadata: Gets metadata about a document - default value True
     @type want_content: boolean
     @param want_content: Gets all the content of the document - default value False
     @type content_as_pages: boolean
     @param content_as_pages: Gets the content of the documents as pages else as a single text blob- default value True
     @rtype: List of dictionaries - [{metadata:'', 'content: ''}, {metadata:'', 'content: ''}, {metadata:'', 'content: ''}]
     @return:  For each document we get its metadata or content or both

    '''
    data_of_pdfs = []
    for file_path in file_paths:
        pdf = {}
        parsed_pdf = parser.from_file(file_path)

        if want_metadata:
            extracted_pdf_metadata = extract_metadata(parsed_pdf["metadata"])
            pdf['metadata'] = extracted_pdf_metadata

        if want_content:
            pdf['content'] = parsed_pdf["content"]

        data_of_pdfs.append(pdf)

    return data_of_pdfs


# def extract_pdf_data(file_paths, want_metadata=True, want_content=False, content_as_pages=True):
#     '''Given a list of path to PDFs, iterate over the list,
#      and for each string, read in the PDF form its path and 
#      return extracted text.

#      The flags might be changed during further development. 
#      Right now they are designed to help in the process of 
#      development and debugging.
#      Developing what details about the document we want to 
#      look at closely - metadata or content or both.
#      It also returns content as pages so that we can decide 
#      which pages to target going forward for information.

#      @type list_of_path_to_pdf: list of string - [str1, str2]
#      @param list_of_path_to_pdf: path of the pdf file to be read
#      @type want_metadata: boolean
#      @param want_metadata: Gets metadata about a document - default value True
#      @type want_content: boolean
#      @param want_content: Gets all the content of the document - default value False
#      @type content_as_pages: boolean
#      @param content_as_pages: Gets the content of the documents as pages else as a single text blob- default value True
#      @rtype: List of dictionaries - [{metadata:'', 'content: ''}, {metadata:'', 'content: ''}, {metadata:'', 'content: ''}]
#      @return:  For each document we get its metadata or content or both

#     '''
#     data_of_pdfs = []
#     for file_path in file_paths:
#         pdf = {}
#         parsed_pdf = parser.from_file(file_path)

#         if want_metadata:
#             extracted_pdf_metadata = extract_metadata(parsed_pdf["metadata"])
#             pdf['metadata'] = extracted_pdf_metadata

#         if want_content:
#             extracted_pdf_content = extract_pdf_content(
#                 file_path, content_as_pages)
#             pdf['content'] = extracted_pdf_content

#         data_of_pdfs.append(pdf)

#     return data_of_pdfs

    # return metadata,results
@Language.factory("language_detector")
def get_lang_detector(nlp, name):
   return LanguageDetector()

def detect_language(content):
    
    # nlp = spacy.load("en")
    nlp.add_pipe('language_detector', last=True)
    doc = nlp(content)

    return doc._.language



def run_hangul(file_path):
    # Start running the tika service
    init()
    # file_path ='./1.pdf'
    metadata_of_pdfs = extract_pdf_data(
        [file_path], want_content=True)
    # print(metadata_of_pdfs[0]['metadata'])
    # print(metadata_of_pdfs[0]['content'])
    clean_doc_content = metadata_of_pdfs[0]['content'] #This is what was used throughout the document
    # print(clean_doc_content, metadata_of_pdfs[0]['metadata'])
    content_as_pages = get_content_pages(file_path)
    if len(content_as_pages) <6:
        doc_title  = get_doc_title(content_as_pages, metadata_of_pdfs[0]['metadata'])
        doc_summary = get_doc_summary(content_as_pages)
    else:
        doc_title  =  get_doc_title(content_as_pages[:3],metadata_of_pdfs[0]['metadata'])
        doc_summary = get_doc_summary(content_as_pages[:6])

    locations = detected_potential_countries(clean_doc_content)
    disasters = get_disasters(clean_doc_content)
    doc_language = detect_language(clean_doc_content)
    doc_report_type = detect_report_type(doc_title)
    # doc_report_type = detect_report_type(file_path)
    if len(content_as_pages) <4:
        display_content =content_as_pages
    else:
        display_content = content_as_pages[:4]

    return {
        'metadata': metadata_of_pdfs[0]['metadata'],
        'Document Language': doc_language,
        'Document Title':doc_title,
        'Document Summary':doc_summary,
        'content': display_content,
        'report_type':doc_report_type,
        'locations': locations,
        'disasters': disasters,

    }
    


def init():
    # Start running the tika service
    tika.initVM()

