import re
import pdfplumber
import docx
import spacy
from typing import Dict, List

# Load SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

def parse_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def parse_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_email(text: str) -> str:
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return match.group(0) if match else ""

def extract_phone(text: str) -> str:
    match = re.search(r"\+?\d[\d\-\s]{8,}\d", text)
    return match.group(0) if match else ""

def extract_skills(text: str, skillset: List[str] = None) -> List[str]:
    if skillset is None:
        skillset = ["Python", "Java", "C++", "Docker", "Kubernetes", 
                    "SQL", "FastAPI", "Flask", "Machine Learning", "React"]
    found = []
    for skill in skillset:
        if skill.lower() in text.lower():
            found.append(skill)
    return found

def extract_info(text: str) -> Dict:
    doc = nlp(text)

    # Extract name (first PERSON entity)
    name = ""
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    return {
        "name": name,
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }
