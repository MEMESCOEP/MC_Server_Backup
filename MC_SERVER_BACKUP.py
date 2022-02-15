# [=========================================================================================================================] #
# [ Minecraft Server Backup program, Written in Python 3                                                                    ] #
# [ Andrew Maney 2022                                                                                                       ] #
# [ MC Version: 1.18.1                                                                                                      ] #
# [ This program copies your ENTIRE server directory into a ZIP file (DO NOT PUT THIS SCRIPT INTO RHE SERVER DIRECTORY!)    ] #
# [ By default, this program will make backups once per hour. You can change this by adding a CMD arg.                      ] #
# [ EX: python MC_SERVER_BACKUP.py 1800    (1800 seconds is equal to 30 minutes )                                           ] #
# [=========================================================================================================================] #


# Imports
from datetime import datetime
import os
import sys
import time
import shutil


# Variables
now = datetime.now() 
date_time = now.strftime("%m-%d-%Y_%H-%M-%S")     # Current Date and time
zip_name = date_time                              # Name of the ZIP file
directory_name = './'                             # This is the name of the directory that you want to make backups of
SleepTime = 3600                                  # 3600 seconds is equal to 1 hour
BACKUP_Dir = "./BACKUPS"                          # Directory where you want to save the backups


# Functions
# Create the backup and move it into the BACKUP_Dir folder
def CreateBackup():
    global SleepTime
    global date_time
    global zip_name
    global now

    try:
        if(not os.path.exists(zip_name + ".zip")):   
            if(not os.path.exists(BACKUP_Dir)):
                print("[WARNING] >> Backup folder \"{}\" Doesn't exist. Creating...".format(BACKUP_Dir))
                os.mkdir(BACKUP_Dir) 
            shutil.make_archive(zip_name, 'zip', directory_name)
            shutil.move(zip_name + ".zip", BACKUP_Dir)
            print("[INFO] >> Created backup \"{}.zip\" at {}".format(zip_name, now.strftime("%m-%d-%Y, %H:%M:%S")))
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

    now = datetime.now() 
    date_time = now.strftime("%m-%d-%Y_%H-%M-%S")
    zip_name = "./" + date_time
    
    CreateBackup()
    print("[INFO] >> Waiting {} seconds to make next backup...\n".format(SleepTime))
    time.sleep(SleepTime)
    BackupTimer()





# Program Initialization
print("Minecraft Server Backup program\nCreated by Andrew Maney\n\n")


# Test if the user entered a command line argument
if(len(sys.argv) > 1):
        if(sys.argv[1] != None):
            if(float(sys.argv[1]) >= 1):
                SleepTime = float(sys.argv[1])
                print("[INFO] >> Setting wait time to {} second(s).".format(sys.argv[1]))
            else:
                print("[WARNING] >> The value \"{}\" is too small! Values must be larger than or equal to 1.".format(sys.argv[1]))
                print("[WARNING] >> Using default wait time.")

# Call the backup function              
BackupTimer()
