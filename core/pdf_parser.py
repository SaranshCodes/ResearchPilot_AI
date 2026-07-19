import fitz
def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    pages=[]
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pages.append({
            'page': page_num+1,
            'text': page.get_text()
        })
    return pages