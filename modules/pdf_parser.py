import fitz


def extract_text_from_pdf(pdf_path):
    """
    Reads a PDF file and returns all the text inside it.
    """

    text = ""

    
    document = fitz.open(pdf_path)

    
    for page in document:
        text += page.get_text()

    
    document.close()

    return text