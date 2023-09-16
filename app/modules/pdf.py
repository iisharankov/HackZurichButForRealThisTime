import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        # Initialize PDF reader
        pdf = PyPDF2.PdfReader(file)

        # Get total number of pages in the PDF
        num_pages = len(pdf.pages)

        # Extract text from each page
        text = ""
        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            text += page.extract_text()

    return text

# # Directory path
# dir_path = "/content/"

# # Get all files from the directory
# all_files = os.listdir(dir_path)

# # Filter only PDF files
# pdf_files = [file for file in all_files if file.endswith('.pdf')]

# # Process each PDF file and store extracted text
# extracted_texts = {}
# for pdf_file in pdf_files:
#     extracted_texts[pdf_file] = extract_text_from_pdf(os.path.join(dir_path, pdf_file))

# # Now, extracted_texts is a dictionary with filenames as keys and extracted text as values.
# # For example, to print the extracted text from the first PDF:
# print(list(extracted_texts.values())[0])

