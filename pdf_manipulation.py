import os
import csv
import importlib
import shutil
import PyPDF2

class DecryptionError(Exception):
    pass


def merge_pdfs(input_folder, output_folder,merged_filename):
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

def merge_pdfs_in_order(files_list,output_folder,merged_filename):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_file in files_list:
        if pdf_file.lower().endswith('.pdf'):
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

    output_path = os.path.join(output_folder, merged_filename)

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

def merge_pdfs_with_bookmarks(input_folder, csv_path, output_folder,merged_filename):
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

    #merged_filename = 'merged.pdf'
    output_path = os.path.join(output_folder, merged_filename)

    if bookmarks:
        for book_title,page in bookmarks:
            merger.add_outline_item(title=book_title,pagenum=page)

    with open(output_path, 'wb') as f:
        merger.write(f)


def convert2pdf(input_dir,output_dir,merged_filename,enhance_img=False,delete_processed_images=False,delete_temp_pdfs=False):
    Image = importlib.import_module('PIL.Image')
    
    
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

def enhance_image(image_path,output_path):
    np = importlib.import_module('numpy')
    cv2 = importlib.import_module('cv2')
    img = cv2.imread(image_path)
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imwrite(output_path,img)
    return img

def enhance_folder(img_dir, output_dir):
    image_paths = sorted(os.listdir(img_dir))
    for image in image_paths:
        output_path = os.path.join(output_dir,image)
        enhance_image(os.path.join(img_dir,image),output_path)

def pdf_splitter(path,out_dir,strt,ed):
    fname = os.path.splitext(os.path.basename(path))[0]
	
    pdf = PyPDF2.PdfReader(path)
    if pdf.isEncrypted:
        if not pdf.decrypt(''):
            simpledialog = importlib.import_module('tkinter.simpledialog')
            password = simpledialog.askstring("Document is encrypted.", "Enter password:",show='*')
            if not pdf.decrypt(password):
                raise DecryptionError

		
    pdf_writer = PyPDF2.PdfWriter()
    for page in range(strt-1,ed):
            pdf_writer.add_page(pdf.pages[page])

    output_filename =os.path.join( out_dir,'{}_pages_{}-{}.pdf'.format(fname, strt,ed))

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)


