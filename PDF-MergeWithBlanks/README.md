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

```
/your_script_directory
│   pdf_merger.py
│
└───input
    │   document1.pdf
    │   document2.pdf
    │   document3.pdf

```

Now run the script (`pdf_merger.py`) using a Python interpreter. You can do this via the terminal or command prompt with the command: 
```console
python pdf_merger.py
```
After running the script, the `input` directory will still contain your original files, and you will find a new file, `output.pdf`, in the base directory. In the `output.pdf`, you'll find the contents of `document1.pdf`, `document2.pdf` followed by a blank page (since it had an odd number of pages), and then `document3.pdf`, for a total of 22 pages.
