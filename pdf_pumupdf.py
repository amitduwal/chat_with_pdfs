import fitz  # PyMuPDF

def get_pdf_text(input_pdf_path, output_text_path):
    text = ""
    pdf_document = fitz.open(input_pdf_path)
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        text += page.get_text()

    pdf_document.close()

    with open(output_text_path, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == '__main__':
    input_pdf_path = "files/Constitution-of-Nepal-_English_-with-1st-Amendment_2.pdf"
    output_text_path = "files/Constitution-of-Nepal-_English_-with-1st-Amendment_2.txt"
    get_pdf_text(input_pdf_path, output_text_path)
    print("PDF to text conversion complete.")