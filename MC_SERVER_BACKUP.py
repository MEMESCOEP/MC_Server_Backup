# [=========================================================================================================] #
# [ Minecraft Server Backup program                                                                         ] #
# [ Andrew Maney 2022                                                                                       ] #
# [ MC Version: 1.18.1                                                                                      ] #
# [ This program backs up a world and creates a ZIP file with the contents.                                 ] #
# [=========================================================================================================] #


# Imports
from datetime import datetime
import os
import sys
import time
import shutil


# Variables
now = datetime.now() 
date_time = now.strftime("%m-%d-%Y_%H-%M-%S")
zip_name = date_time
directory_name = './world'
SleepTime = 3600
BACKUP_Dir = "./BACKUPS"


# Functions
# Create the backup and move into the BACKUP_Dir folder 
def CreateBackup():
    global SleepTime
    global date_time
    global zip_name
    global now

    try:
        if(not os.path.exists(zip_name + ".zip")):   
            if(not os.path.exists(BACKUP_Dir)):
                os.mkdir(BACKUP_Dir) 
            shutil.make_archive(zip_name, 'zip', directory_name)
            shutil.move(zip_name + ".zip", BACKUP_Dir)

            print("[INFO] >> Created backup \"{}\" at {}".format(zip_name, date_time))
        else:
            print("[ERROR] >> Failed to create backup! Details: File already exists")
    except Exception as EX:
        print("[ERROR] >> Failed to create backup! Details: {}".format(EX))


# Create a backup at the selected time interval
def BackupTimer():
    global SleepTime
    global date_time
    global zip_name
    global now
    
    if(len(sys.argv) > 1):
        if(sys.argv[1] != None):
            SleepTime = int(sys.argv[1])
    now = datetime.now() 
    date_time = now.strftime("%m-%d-%Y_%H-%M-%S")
    zip_name = "./" + date_time
    
    CreateBackup()
    time.sleep(SleepTime)
    BackupTimer()


# Initialize the program
BackupTimer()
