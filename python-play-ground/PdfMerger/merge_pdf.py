

from pypdf import PdfWriter

def merge():
    merger = PdfWriter()

    for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()

if __name__ == '__main__':
    merge()