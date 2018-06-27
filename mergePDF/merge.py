import os
import re
import PyPDF2

def search_merge_message(path):
    term = re.compile("MERGERENAME_.*?\.txt")
    merge_folders = []
    for dirpath, _, filenames in os.walk(path):
        for filename in [f for f in filenames if term.match(f)]:
            merge_folders.append(dirpath)
    return merge_folders

def get_pdf_files(path):
    all_files = []
    for dirpath,_, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(".pdf")]:
            all_files.append(os.path.join(dirpath,filename))
    return all_files

def merge_pdf_files(pdf_files):

    output = PyPDF2.PdfFileWriter()
    
    for pdf_file in pdf_files:
        temp_file = PyPDF2.PdfFileReader(pdf_file,'rb')
        for page in temp_file.pages:
            output.addPage(page)
    return output

def save_pdf(pdf_file,merged_file_name):
    result_pdf = open(merged_file_name,'wb')
    pdf_file.write(result_pdf)


#path = r"C:\Users\benedikt.rauscher\Documents\tempToDelete"
path = r'C:\Users\benedikt.rauscher\Documents'
merged_file_name = r"test.pdf"
merge_folders = search_merge_message(path)

for i in merge_folders:
    pdf_files = get_pdf_files(i)
    pdf_file = merge_pdf_files(pdf_files)
    merged_file_name = os.path.join(i,merged_file_name)
    save_pdf(pdf_file,merged_file_name)