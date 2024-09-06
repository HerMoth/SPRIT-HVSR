import os #os module provides a way of using operating system dependent functionality
import shutil #shutil module provides a higher level interface that is easier to use

#log directory
log_dir = "/opt/log/"

#gets the current date for the log file
from datetime import date 
today = date.today().strftime("%Y-%m-%d")

#creates the archive directory
archive_dir = "/home/pi/shake_logs/" + today 

#checks if the archive directory exists, if not create it
if not os.path.exists(archive_dir):
    os.makedirs(archive_dir)

#loop through the log files in the log directory
for filename in os.listdir(log_dir):

#copy the log files to the archive directory   
    shutil.copy(os.path.join(log_dir, filename),
os.path.join(archive_dir, filename))
    
print("Logs have been archived to " , archive_dir)
