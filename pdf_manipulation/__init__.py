import os
# import importlib
import shutil
import PyPDF2
import numpy as np
import cv2
from PIL import Image

def merge_pdfs(input_folder: str, output_folder: str,merged_filename: str) -> None:
    """
    Merge all PDFs in a folder into a single PDF file. Order is determined by the sorting in the OS.

    Args:
        input_folder (str): Folder containing PDF files to merge.
        output_folder (str): Folder to save the merged PDF file.
        merged_filename (str): Name of the merged PDF file.

    Returns:
        None

    """
    pdf_writer = PyPDF2.PdfWriter()

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            pdf_file = os.path.join(input_folder, filename)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

    output_path = os.path.join(output_folder, merged_filename)

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

def merge_pdfs_in_order(files_list: list,output_folder: str,merged_filename: str) -> None:
    """
    Merge PDFs in a list into a single PDF file. Order is determined by the order of the list.

    Args:
        files_list (list): List of PDF filenames to merge.
        output_folder (str): Folder to save the merged PDF file.
        merged_filename (str): Name of the merged PDF file.
    
    Returns:
        None
    """
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_file in files_list:
        if pdf_file.lower().endswith('.pdf'):
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

    output_path = os.path.join(output_folder, merged_filename)

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

def convert2pdf_with_order(input_list: list,output_dir: str,merged_filename:str, enhance_img:bool=False):
    """
    Convert a list of images to PDFs and merge them in the order of the list. Optionally enhance the images by converting to greyscale and filtering lower values before conversion.

    Args:
        input_list (list): List of image filenames to convert to PDFs.
        output_dir (str): Folder to save the converted PDFs and the merged PDF file.
        merged_filename (str): Name of the merged PDF file.
        enhance_img (bool): Enhance the images before conversion. Default is False.

    Returns:
        None

    """

    if enhance_img:
        processed_image_path = os.path.join(output_dir,"enhanced_images")

        if os.path.exists(processed_image_path):
            shutil.rmtree(processed_image_path)
            os.makedirs(processed_image_path)
        else:
            os.makedirs(processed_image_path)

    converted_pdfs_path = os.path.join(output_dir,"converted_pdfs")
    if os.path.exists(converted_pdfs_path):
        shutil.rmtree(converted_pdfs_path)
        os.makedirs(converted_pdfs_path)
    else:
        os.makedirs(converted_pdfs_path)

    pdf_list = []

    for input_image in input_list:
        if input_image.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            img_name = os.path.basename(input_image)
            pdf_list.append(os.path.join(converted_pdfs_path,img_name)+'.pdf')
            pdf = open(os.path.join(converted_pdfs_path,img_name)+'.pdf', 'wb')
            if enhance_img:
                image = enhance_image(input_image,os.path.join(output_dir,"enhanced_images",img_name))
                image = Image.fromarray(image)
            else:
                image = Image.open(input_image)
            image = image.convert('RGB')
            image.save(pdf, 'PDF')
            pdf.close()
    
    merge_pdfs_in_order(pdf_list,output_dir,merged_filename)
    if enhance_img:
        shutil.rmtree(processed_image_path)

    shutil.rmtree(converted_pdfs_path)

def convert2pdf(input_dir: str,output_dir: str,merged_filename: str,enhance_img: bool=False,delete_processed_images: bool=False,delete_temp_pdfs: bool=False) -> None:
    """
    Convert images in a folder to PDFs and merge them into a single PDF file. Optionally enhance the images by converting to greyscale and filtering lower values before conversion.

    Args:
        input_dir (str): Folder containing images to convert to PDFs.
        output_dir (str): Folder to save the converted PDFs and the merged PDF file.
        merged_filename (str): Name of the merged PDF file.
        enhance_img (bool): Enhance the images before conversion. Default is False.
        delete_processed_images (bool): Delete the processed images after conversion. Default is False.
        delete_temp_pdfs (bool): Delete the temporary PDF files after merging. Default is False.
    
    Returns:
        None

    """
    
    image_paths = sorted(os.listdir(input_dir))

    if enhance_img:
        processed_image_path = os.path.join(output_dir,"enhanced_images")

        if os.path.exists(processed_image_path):
            shutil.rmtree(processed_image_path)
            os.makedirs(processed_image_path)
        else:
            os.makedirs(processed_image_path)

    converted_pdfs_path = os.path.join(output_dir,"converted_pdfs")
    if os.path.exists(converted_pdfs_path):
        shutil.rmtree(converted_pdfs_path)
        os.makedirs(converted_pdfs_path)
    else:
        os.makedirs(converted_pdfs_path)

    for input_image in image_paths:
        if input_image.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            pdf = open(os.path.join(converted_pdfs_path,input_image)+'.pdf', 'wb')
            if enhance_img:
                image = enhance_image(os.path.join(input_dir,input_image),os.path.join(output_dir,"enhanced_images",input_image))
                image = Image.fromarray(image)
            else:
                image = Image.open(os.path.join(input_dir,input_image))
            image = image.convert('RGB')
            image.save(pdf, 'PDF')
            pdf.close()
    
    merge_pdfs(converted_pdfs_path,output_dir,merged_filename)

    if delete_processed_images and enhance_img:
        shutil.rmtree(processed_image_path)
    if delete_temp_pdfs:
        shutil.rmtree(converted_pdfs_path)

def enhance_image(image_path: str,output_path: str) -> np.ndarray:
    """
    Enhance an image by converting to greyscale, denoising, and thresholding.

    Args:
        image_path (str): Path to the image file.
        output_path (str): Path to save the enhanced image.
    
    Returns:
        np.ndarray: Enhanced image as a NumPy array.

    """
    img = cv2.imread(image_path)
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imwrite(output_path,img)
    return img

def enhance_images(input_dir: str,output_dir: str) -> None:
    """
    Enhance all images in a folder by converting to greyscale, denoising, and thresholding.

    Args:
        input_dir (str): Folder containing images to enhance.
        output_dir (str): Folder to save the enhanced images.
    
    Returns:
        None

    """
    image_paths = sorted(os.listdir(input_dir))
    for image in image_paths:
        enhance_image(os.path.join(input_dir,image),os.path.join(output_dir,image))

def pdf_splitter(path:str,out_dir:str,start_page:int,end_page:int) -> None:
    """
    Split a PDF file into multiple PDF files based on the start and end page numbers.

    Args:
        path (str): Path to the PDF file.
        out_dir (str): Folder to save the split PDF files.
        start_page (int): Start page number.
        end_page (int): End page number.
    
    Returns:
        None

    """
    fname = os.path.splitext(os.path.basename(path))[0]
    
    pdf = PyPDF2.PdfReader(path)
    if pdf.isEncrypted:
        if not pdf.decrypt(''):
            password = input("Document is encrypted. Enter password: ")
            # simpledialog = importlib.import_module('tkinter.simpledialog')
            # password = simpledialog.askstring("Document is encrypted.", "Enter password:",show='*')
            if not pdf.decrypt(password):
                raise Exception("Decryption failed.")

        
    pdf_writer = PyPDF2.PdfWriter()
    for page in range(start_page-1,end_page):
            pdf_writer.add_page(pdf.pages[page])

    output_filename =os.path.join( out_dir,'{}_pages_{}-{}.pdf'.format(fname, start_page,end_page))

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
