.. _usage:

Usage
=====

To use the package, import the functions as follows. Look at the :doc:`functions` documentation for more information on how to use them.

Merge PDFs
----------

.. code-block:: python

    from pdf_manipulation import merge_pdfs

    input_folder = ...             # Folder contatining PDFs to merge
    output_folder = ...            # Folder to store the output
    merged_filename = "merged.pdf" # File name for the merged file

    merge_pdfs(input_folder,output_folder,merged_filename)

Split PDFs
----------

.. code-block:: python

    from pdf_manipulation import pdf_splitter

    path = ...                     # Path to PDF to split
    output_folder = ...            # Folder to store the output
    start_page = 1                 # Beginning page to split
    end_page = 5                   # Ending page to split

    pdf_splitter(path,output_folder,start_page,end_page)

Convert Image to PDF
--------------------

.. code-block:: python

    from pdf_manipulation import convert2pdf

    input_dir = ...            # Folder containing images to convert to PDFs.
    output_dir = ...           # Folder to save the converted PDFs and the merged PDF file.
    merged_filename = ...      # Name of the merged PDF file.
    enhance_img = True         # (Optional) Enhance the images before conversion. Default is False.

    convert2pdf(input_dir,output_dir,merged_filename,enhance_img)
