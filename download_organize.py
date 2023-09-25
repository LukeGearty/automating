import os
import magic
import shutil
# a program that will take anything downloaded, check if
# they are jpgs or pdfs,
# and organize them into folders based on filetype. Uses the
# magic library to check files
# get the directory
download_file = "C://Path//to//downloads"
os.chdir(download_file)
# list directory
directory = os.listdir(download_file)
# create the jpg file on desktop if it doesn't exist
def create_jpeg_folder():
    try:
        directory_path = "C://Path//To//Desktop"
        jpeg_directory = "JPEG_Folder"
        jpeg_path = os.path.join(directory_path,jpeg_directory)
        os.mkdir(jpeg_path)
    except WindowsError:
        exit
    return jpeg_path
def create_pdf_folder():
    try:
        directory_path = "C://Path//To//Desktop"
        pdf_folder = "PDF_Folder"
        pdf_path = os.path.join(directory_path, pdf_folder)
        os.mkdir(pdf_path)
    except WindowsError:
        exit
    return pdf_path
create_jpeg_folder()
create_pdf_folder()
for files in directory:
    file_type = magic.from_file(files)
    list = file_type.split()
    # check if it is a pdf or jpeg and add it to the proper folder
    if list[0] == "PDF":
        shutil.move(files,create_pdf_folder())
    elif list[0] == "JPEG":
        shutil.move(files,create_jpeg_folder())
