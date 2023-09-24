#pdf_merge

This directory contains a simple graphical interface for merging PDF files.

# launch via python

This GUI was coded with python 3.10.7

first open your terminal then clone this directory with:

```
git clone <repo url>
```
Once you have cloned the directory, move to this folder:

```
cd pdf_fusion
```

then install the necessary packages:

```
pip install -r requirements.txt
```

then launch the interface:

```
python fusion_pdf_interface.py
```

# Manual

First, put all the files to be merged in the same folder.

>:warning: the merge will follow the alphabetical order of the file titles. Consider renaming them accordingly.

once the interface is launched you should see the following window open:

<p align="center">
<img src="img/interface.png" alt="ONE-PIX principle" width="500"/>
</p>

- select by hard pressing the top button the folder containing the pdfs to be merged
- section the folder in which you want to save the merged pdfs
- press the concatenate pdf button to start the merger.

the graphical interface should close and a pdf file named concatenate_pdf should have been created in the previously selected save folder.