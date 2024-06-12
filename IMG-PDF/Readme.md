# IMG to PDF

You will need the pillow package

```console
pip install pillow
```

## Usage of img2pdf.py

The img2pdf.py script converts img files to pdf and merges them to form one pdf file

Copy the image files to "input" folder

Open terminal and type the following (or double click on img2pdf.py on Windows)

```console
python img2pdf.py
```

The result will come out as "out.pdf"

## Example

Suppose you have the following file structure

- img2pdf.py
- input
  - file1.jpg
  - file2.jpg
  - file3.jpg

After running the script, the following file will be generated:

- pdf_merger.py
- input
  - file1.jpg
  - file2.jpg
  - file3.jpg
- out.pdf

The out.pdf file will contain the merged content of file1.jpg, file2.jpg, and file3.jpg.
