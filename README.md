# PDF-manipulation

This application can

1. Merge different PDFs into one. The order is based on alphabetical order of the filenames
2. Convert image files to PDF and merge them into one. This has a feature of enhancing the images for clearer text.
3. Split one pdf at certain page numbers


## Usage

### Graphical Application

Run main.py by either

- Double clicking on `main.py`

- Run
```console
python main.py
```

### Command line

The file `pdf_manipulation.py` can be used as a module with the following functions. There is a template in `cmd_line.py` to demonstrate the use.

Functions

1. `merge_pdfs(input_folder, output_folder)`: This function merges all PDF files in the given input folder and writes the merged PDF to the output folder.

2. `merge_pdfs_with_bookmarks(input_folder, csv_path, output_folder)`: This function merges all PDF files in the given input folder, adds bookmarks from a CSV file, and writes the merged PDF to the output folder.

3. `convert2pdf(input_dir,output_dir,enhance_img=False,delete_processed_images=False,delete_temp_pdfs=False)`: This function converts all images in the input directory to PDFs, optionally enhances the images before conversion, and writes the PDFs to the output directory. It can also optionally delete the processed images and temporary PDFs.

4. `enhance_image(image_path,output_path)`: This function enhances an image by normalizing it, denoising it, converting it to grayscale, and applying adaptive thresholding. The enhanced image is saved to the output path.

5. `enhance_folder(img_dir, output_dir)`: This function enhances all images in the given directory using the enhance_image function and saves the enhanced images to the output directory.

6. `pdf_splitter(path,out_dir,strt,ed)`: This function splits a PDF file from the start page to the end page and writes the split PDF to the output directory.

## Requirements
The script requires the following dependencies:

- Numpy

- PyPDF2: A Python library for reading and manipulating PDF files.

For image processing and manipulation

- Pillow: Pillow is a Python library that provides image processing capabilities, such as opening, manipulating, and saving different image file formats.

- OpenCV: OpenCV is a popular computer vision library that provides various functions and algorithms for image and video processing.

Ensure that the required dependencies are installed by running the following

```console
pip install numpy
pip install PyPDF2
pip install pillow
pip install opencv-python
```
