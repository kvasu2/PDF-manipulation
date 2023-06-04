add files to be merged into input folder

run PDF_merger.py

This will take all the file in the input folder and merger them by adding a blank when the files have odd number of pages

# PDF Merger with Even Page Count

This Python script utilizes the PyPDF2 library to merge multiple PDF files, while ensuring that each document has an even number of pages.

The script obtains the current script's directory and constructs paths for the input directory (containing PDF files to be merged) 

The resulting output file will be a PDF that is a merge of all PDFs found in the input directory. If any of these PDFs have an odd number of pages, a blank page will be appended to ensure the merged document maintains an even number of pages.

## Example

For the script to work correctly, you must have a directory named `input` in the same location as the script itself. This directory should contain the PDF files you want to merge.

Here's an example of how to use the script:

Let's say you have three PDF files you want to merge:

- document1.pdf (10 pages)
- document2.pdf (7 pages)
- document3.pdf (4 pages)

Place these files in the `input` directory:

|-- src
│   |--   pdf_merger.py
│   |--input
    │   document1.pdf
    │   document2.pdf
    │   document3.pdf

