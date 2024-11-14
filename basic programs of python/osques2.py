
from pypdf import PdfWriter
import os

merge= PdfWriter()
mydir="xpics"
pdfs=os.listdir(mydir)

for file in  pdfs:
    path= os.path.join(mydir,file)
    merge.append(path)

merge.write("resultmerge.pdf")

merge.close()

