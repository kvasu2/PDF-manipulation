[![Documentation Status](https://readthedocs.org/projects/pdf-manipulation/badge/?version=latest)](https://pdf-manipulation.readthedocs.io/?badge=latest)

# PDF-manipulation

The project contains code for manipulating pdfs with simple functions in python. Refer [documentation](https://pdf-manipulation.readthedocs.io/) for installation and usage.

## Installation

```bash
pip install pdf-manipulation
```

## Usage
```python
from pdf_manipulation import merge_pdfs, pdf_splitter, convert2pdf, enhance_image

input_folder = ...             # Folder contatining PDFs to merge
output_folder = ...            # Folder to store the output
merged_filename = "merged.pdf" # File name for the merged file

merge_pdfs(input_folder,output_folder,merged_filename)

```
