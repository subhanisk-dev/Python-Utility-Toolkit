from PyPDF2 import PdfMerger
import os

merger = PdfMerger()
files = []

print("Enter the PDF file names one by one (type 'done' to finish)")

while True:
    name = input("PDF file : ").strip()
    if name.lower() == "done":
        break
    elif os.path.isfile(name) and name.lower().endswith(".pdf"):
        files.append(name)
    else:
        print("File not found or not a PDF.")

if len(files) < 2:
    print("At least two PDF files are required to merge.")
else:
    for f in files:
        merger.append(f)
    output_name = input("Enter output file name (example: merged.pdf) : ").strip()+".pdf"

    # Get the folder of the first PDF
    folder = os.path.dirname(os.path.abspath(files[0]))

    # Save merged PDF in the same folder
    output = os.path.join(folder, output_name)

    merger.write(output)
    merger.close()
    print(len(files), "files merged successfully into", output)
