# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:25:30 2021

@author: grussias
"""
import os 
from tkinter import filedialog
from tkinter import *
import glob
import  PyPDF2 as pi

chemin_script = os.getcwd()
root = Tk()
root.withdraw()
root.attributes('-topmost', 1)
chemin_mesure = filedialog.askdirectory(title = "ouvrir le dossier contenant les mesures", initialdir = chemin_script)


fout="test.pdf"

os.chdir(chemin_mesure)

files_list = sorted(glob.glob('*.pdf'),key=os.path.getmtime)

merger = pi.PdfMerger()

for pdf in files_list:
    merger.append(open(pdf, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)

os.chdir(chemin_script)