# PDF Merger

## Usage

The pdf_merger.py script is a Python program that merges multiple PDF files into a single PDF file.

Copy the pdf's to "input"

Open terminal and type the following (or double click on pdf_merger.py on Windows)

```console
python pdf_merger.py
```

The result will come out as "out.pdf"

## Example

Suppose you have the following file structure

- pdf_merger.py
- input
  - file1.pdf
  - file2.pdf
  - file3.pdf

After running the script, the following file will be generated:

- pdf_merger.py
- input
  - file1.pdf
  - file2.pdf
  - file3.pdf
- out.pdf

The out.pdf file will contain the merged content of file1.pdf, file2.pdf, and file3.pdf.

## Code Explanation

1. Defining the merger Function
The merger function takes an output_path and a list of input_paths as parameters. It performs the merging of PDF files using the PdfFileWriter and PdfFileReader classes from PyPDF2.

2. Gathering Input PDF Files
The script retrieves the current directory path and constructs the path to the input directory, which is assumed to be in the same directory as the script. It then retrieves a sorted list of all files in the input directory.

3. Merging PDF Files
The script iterates over the input files and adds each page from each PDF file to the pdf_writer object using the addPage method. The pdf_writer object is an instance of PdfFileWriter.

4. Writing the Merged PDF File
The merged PDF file is written to the output_path specified in the script. The pdf_writer object's contents are written to a file using the write method, and the file is closed automatically after writing.
