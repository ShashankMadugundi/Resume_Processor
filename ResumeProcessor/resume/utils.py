import re
from docx import Document
from PyPDF2 import PdfReader


def extract_resume_data(file):
    if file.name.endswith('.pdf'):
        text = extract_text_from_pdf(file)
    elif file.name.endswith('.docx'):
        text = extract_text_from_docx(file)
    else:
        return None 

    email = extract_email(text)
    mobile_number = extract_mobile_number(text)

    first_name = extract_name(text)
    
    return {
        'first_name': first_name,
        'email': email,
        'mobile_number': mobile_number
    }

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def extract_text_from_docx(file):
    document = Document(file)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + '\n'
    return text


def extract_email(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
    match = re.search(email_pattern, text)
    return match.group(0) if match else None

def extract_mobile_number(text):
    mobile_pattern = r"\+?\(?\d{1,4}\)?[\s\-]?\d{1,4}[\s\-]?\d{1,4}[\s\-]?\d{1,4}"
    match = re.search(mobile_pattern, text)
    return match.group(0) if match else None


import re


import spacy
from spacy.matcher import Matcher

def extract_name(resume_text):
    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)

    patterns = [
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}],  
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],  
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}] 
    ]


    for pattern in patterns:
        matcher.add('NAME', patterns=[pattern])

    doc = nlp(resume_text)
    matches = matcher(doc)


    for match_id, start, end in matches:
        span = doc[start:end]
        first_name = span.text.split()[0]
        return first_name

    return None
