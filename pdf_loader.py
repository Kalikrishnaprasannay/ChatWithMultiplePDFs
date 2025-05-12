import PyPDF2
from typing import List

def extract_text_from_pdfs(files: List) -> str:
    all_text = ""
    for file in files:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            all_text += page.extract_text() or ""
    return all_text
