#@author- SIdra Effendi
import tika
from tika import parser
import spacy
from .disaster_detection import get_disasters
from collections import Counter
from .get_file_metadata import extract_metadata

nlp = spacy.load('en_core_web_sm')



# def extract_metadata(pdf_metadata):
#     metadata_final = {}
#     for my_key, my_value in pdf_metadata.items():
#         if my_key in ['Author', 'creator']:
#             metadata_final['Author'] = my_value
#         elif my_key in ['xmpTPg:NPages']:
#             metadata_final['No.of Pages'] = my_value
#         elif my_key in ['resourceName']:
#             metadata_final['Document Title'] = my_value.replace(
#                 "b'", '').replace(".pdf'", "")  # create contenders for titles
#         elif my_key in ['Keywords', 'subject']:
#             metadata_final['Subject'] = my_value
#         elif my_key in ['dc:title', 'title']:
#             metadata_final[my_key] = my_value
#         elif my_key in ['Content-Type', 'Creation-Date', 'producer']:
#             metadata_final[my_key] = my_value
#         # else:
#         # 	metadata_final[my_key] = my_value
#     return metadata_final


def extract_pdf_content(pdf_path, content_as_pages):

    if content_as_pages:
        raw_xml = parser.from_file(pdf_path, xmlContent=True)
        body = raw_xml['content'].split('<body>')[1].split('</body>')[0]
        body_without_tag = body.replace("<p>", "").replace("</p>", "\n").replace("<div>", "").replace("</div>","\n").replace("<p />","\n")
        text_pages = body_without_tag.split("""<div class="page">""")[1:]
        num_pages = len(text_pages)
        print(num_pages)
        if num_pages==int(raw_xml['metadata']['xmpTPg:NPages']) : #check if it worked correctly
            for i in range(5):
            # for i in range(num_pages):
                print('page number: '+ str(i+1))
                print(text_pages[i].replace("\n", ""))
                print('\n')
        pdf_content = body_without_tag
    else:
        parsed_pdf = parser.from_file(pdf_path)
        # parsed_data_full = parser.from_file(pdf_path,xmlContent=True) 
        # parsed_data_full = parsed_data_full['content']
        # print(parsed_data_full)
        # print(parsed_pdf["content"])
        pdf_content= parsed_pdf["content"].replace("\n", "")
        # return parsed_pdf["content"]
    return pdf_content


def extract_pdf_data(file_paths, want_metadata=True, want_content=False, content_as_pages=True):
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
            # print(extracted_pdf_metadata)

        if want_content:
            extracted_pdf_content = extract_pdf_content(
                file_path, content_as_pages)
            pdf['content'] = extracted_pdf_content

        data_of_pdfs.append(pdf)

    return data_of_pdfs

    # return metadata,results

# def extract_summary(content,text):


def detect_location(content):
    nlped = nlp(content)
	
    locations = [(x.text.replace('\n', ''), x.label_)
                 for x in nlped.ents if x.label_ == 'GPE']
    # most_common = [(x, z) for ((x, y), z) in Counter(locations).most_common()]
    most_common_location = Counter(locations).most_common(3)
    return most_common_location


def run_hangul(file_path):
    # Start running the tika service
    init()
    # file_path ='./1.pdf'
    metadata_of_pdfs = extract_pdf_data(
        [file_path], want_content=True, content_as_pages=False)
    # print(metadata_of_pdfs[0]['metadata'])
    locations = detect_location(metadata_of_pdfs[0]['content'])
    disasters = get_disasters(metadata_of_pdfs[0]['content'])

    return {
        'metadata': metadata_of_pdfs,
        'locations': locations,
        'disasters': disasters
    }
    # print(metadata_of_pdfs)
    # 	extract_summary(content,text)
    #
    # separate the content and metadat and process accordingly
    # display the metadata
    # use the content for language detection


def init():
    # Start running the tika service
    tika.initVM()

# print(run_hangul('a'))
