import os
from datetime import date, datetime

# a program that will delete files from downloads folder if it is older than 1 week
# get today's date
today = date.today()

# set the file path to a variable
download_file = "C://path//to//downloads"
os.chdir(download_file)
# list the directory
directory = os.listdir(download_file)
#loop through the directory
for files in directory:
#     # get the files date
    date_file = os.path.getmtime(files)
     # convert
    converted = datetime.fromtimestamp(date_file)
    # strip it so that it is just the date with time as well
    converted = datetime.date(converted)
    # use a delta to compare today's date to converted, then use if statement with delta.days
    delta = today - converted
    try:
        if delta.days > 7:
            os.remove(files)
    except PermissionError:
        continue
