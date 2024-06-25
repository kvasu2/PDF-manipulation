.. pdf-manipulation documentation master file, created by
   sphinx-quickstart on Tue Jun 25 12:27:31 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PDF-Manipulation's documentation!
============================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   Home <self>
   functions


Introduction
============

This package is a collection of functions that can be used to manipulate PDF files. The functions are written in Python and can be used to merge PDFs, split PDFs, convert images to PDFs and enhance the images for better text visibility.

.. _installation:

Installation
============

To install the package, run the following command:

.. code-block:: bash

    pip install pdf-manipulation

.. _usage:

Usage
=====

To use the package, import the functions as follows:

.. code-block:: python

    from pdf_manipulation import merge_pdfs, pdf_splitter, convert2pdf, enhance_image

Look at the :doc:`functions` documentation for more information on how to use them.
