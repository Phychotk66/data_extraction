import fitz

def ingest_pdf(file_path):
    doc = fitz.open(file_path)
    pages = []
    for page in doc:
        pix = page.get_pixmap()
        img = pix.tobytes("png")
        pages.append(img)
    doc.close()
    return pages