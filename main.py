import os,magic,shutil
from datetime import date, datetime

# automating the processes of the other two downloads file
def exec_file(file):
     with open(file) as df:
         print(f"Executing {file} now!")
         exec(df.read())
         print(f"{file} executed!")
def main():
    exec_file("organize_downloads.py")
    exec_file("clean_download.py")


if __name__=="__main__":
    main()
