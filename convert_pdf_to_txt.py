from PyPDF2 import PdfReader

def get_pdf_text(input_pdf_path, output_text_path):
    text = ""
    pdf_reader= PdfReader(input_pdf_path)
    for page in pdf_reader.pages:
        text += page.extract_text()
    with open(output_text_path, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == '__main__':
    input_pdf_path="constitution.pdf"
    output_text_path = "constitution.txt"
    get_pdf_text(input_pdf_path, output_text_path)
    print("PDF to text conversion complete.")