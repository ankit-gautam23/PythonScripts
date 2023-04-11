# PDF to Images
# pip install PyMuPDF
import fitz

def pdf_to_image_converter(pdf_file):
    doc = fitz.open(pdf_file)
    for p in doc:
        pixels = p.get_pixmap()
        image = f"page{p.number}.png"
        pixels.writePNG(image)

pdf_to_image_converter("test.pdf")
