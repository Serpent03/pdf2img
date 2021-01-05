# le modules

from wand import image      #pretty simple. convert png/jpg to dds.
from pdf2image import convert_from_path, convert_from_bytes  # main pdf to image conversion utility
from PIL import Image # image handling module
import glob 
import subprocess # Instead of OS I used glob and subprocess, as on compilation, OS operation made windows think this script was a virus
from tkinter import Tk # for pdf file selection
from tkinter.filedialog import askopenfilename
Tk().withdraw() # don't want any tkinter window. straight to file path

selectedPdf = askopenfilename() # selected pdf
path = 'tmpdata' # where the program will output temporary file data it extracts from pdf. folder will be made in same directory as the python script

# set this up
if path not in (glob.glob('*/')):
    p=subprocess.Popen("mkdir tmpdata", shell=True)
    p.wait()


# functions, muhahaha
def single_page(pg):
    pg = int(pg)
    img = convert_from_path(selectedPdf, thread_count = 4, size = (1024, 2048), first_page = pg, output_folder = path) # slected pdf, run on 4 threads, image size = 1024(width) by 2048(height)
    img[0].save(f'{pg}.jpg', 'JPEG') # image type. .jpg = JPEG. .png = PNG. jpg is faster than png

def multi_pages(fPg, lPg):
    fPg = int(fPg)
    lPg = int(lPg)
    pageNum = fPg
    img = convert_from_path(selectedPdf, thread_count = 4, size = (1024, 2048), first_page=fPg, last_page=lPg, output_folder=path)

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

## check and assign for single, multiple or range of pdf to convert into image.
if not isinstance(pages, list): # single page
    single_page(pages)
else:
    if fileType == 0: # multiple pages
        for pdfScannedPages in pages:
            single_page(pdfScannedPages) # run the single page converter, but for multiple pages instead of bulk

    elif fileType == 1: # bulk pages
        pages.sort()
        multi_pages(pages[0], pages[1]) # call first page and last page for bulk
        





input("Press enter to exit..")
