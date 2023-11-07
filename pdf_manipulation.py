import os
import PyPDF2
import csv

def merge_pdfs(input_folder, output_folder):
    merger = PyPDF2.PdfMerger()

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_file = os.path.join(input_folder, filename)
            with open(pdf_file, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                merger.append(reader)

    merged_filename = 'merged.pdf'
    output_path = os.path.join(output_folder, merged_filename)

    with open(output_path, 'wb') as f:
        merger.write(f)

def merge_pdfs_with_bookmarks(input_folder, csv_path, output_folder):
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        merger = PyPDF2.PdfMerger()
        bookmarks = []

        for row in reader:
            pdf_filename = row['filename']
            pdf_path = os.path.join(input_folder, pdf_filename)
            bookmark_title = row['bookmark_title']
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                if bookmark_title:
                    bookmarks.append((bookmark_title,len(merger.pages)))
                merger.append(reader)

    merged_filename = 'merged.pdf'
    output_path = os.path.join(output_folder, merged_filename)

    if bookmarks:
        for book_title,page in bookmarks:
            merger.add_outline_item(title=book_title,pagenum=page)

    with open(output_path, 'wb') as f:
        merger.write(f)
