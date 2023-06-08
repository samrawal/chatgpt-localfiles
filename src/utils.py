import os
import PyPDF2
from docx import Document


def get_filenames(path):
    filepaths = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepaths.append(os.path.normpath(os.path.join(dirpath, filename)))
    return filepaths


def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


def read_file(filepath):
    if filepath.endswith(".pdf"):
        with open(filepath, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            content = ""
            for page in range(len(reader.pages)):
                content += reader.pages[page].extract_text().strip() + " " 
        return content
    elif filepath.endswith(".docx"):
        doc = Document(filepath)
        content = " ".join([paragraph.text for paragraph in doc.paragraphs])
        return content
    else:
        with open(filepath, "r") as file:
            content = file.read()
        return content
