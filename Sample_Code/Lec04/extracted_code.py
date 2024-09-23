import fitz

def read_pdf(pdf_path):
  doc = fitz.open(pdf_path)
  text = ""

  for page in doc:
    text += page.get_text()

  return text

if __name__ == "__main__":
  pdf_file_path = r"Sample_Code/Lec04/saoke.pdf" 
  extracted_text = read_pdf(pdf_file_path)
  print(extracted_text)