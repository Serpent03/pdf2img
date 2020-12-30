# le modules

from wand import image      #pretty simple. convert png/jpg to dds.
from pdf2image import convert_from_path, convert_from_bytes  # needs 
from PIL import Image
import os
from os import walk, listdir
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()

home = os.getcwd()
path = 'tmpdata'
selectedPdf = askopenfilename()

# set this up
dirs = os.listdir()
if path in dirs:
    pass
else:
    os.mkdir(path)
    os.chdir(path)

# functions, muhahaha
def single_page(pg):
    pg = int(pg)
    img = convert_from_path(selectedPdf, size = (1024, 2048), first_page = pg-1, last_page = pg, output_folder = path)
    img[0].save(f'{pg}.jpg', 'JPEG')

def multi_pages(fPg, lPg):
    fPg = int(fPg)
    lPg = int(lPg)
    pageNum = fPg
    img = convert_from_path(selectedPdf, size = (1024, 2048), first_page=fPg, last_page=lPg, output_folder=path)

    for imgFiles in img:
        imgFiles.save(f'{pageNum}.jpg', 'JPEG')
        pageNum += 1

# get yo pages in, half the price fo' everythin'
pgSelection = input("Which page(s)? For multiple, separsate by comma, for range, separate by hyphen.\n~ ")

for chars in pgSelection:
    pgSelection = pgSelection.replace(' ', '')
    if ',' in pgSelection:
        pages = (pgSelection.split(","))
        fileType = 0 # type is multiple pdf page
    elif '-' in pgSelection:
        pages = (pgSelection.split("-"))
        fileType = 1 # type is bulk pdf pages
    else:
        pages = pgSelection

# check and assign for single, multiple or range of pdf to convert into image.
if not isinstance(pages, list): # single page
    single_page(pages)
else:
    if fileType == 0: # multiple pages
        for pdfScannedPages in pages:
            single_page(pdfScannedPages) # run the single page converter, but for multiple pages instead of bulk

    elif fileType == 1: # bulk pages
        pages.sort()
        multi_pages(pages[0], pages[1]) # call first page and last page for bulk
        

