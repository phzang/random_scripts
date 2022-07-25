# Reolink Camera sends videos via FTPS
# Script removes DAYS_AGO days ago directory to save space on NAS
# Folders are separated by /camera_folder/year/month/day e.g. /camera_folder/2022/06/20
# 7 DAYS_AGO from 2022/06/20 would remove 2022/06/13 directory
# Tested on Windows 10 and Linux (Unraid)

from dateutil.relativedelta import *
from datetime import *
import os.path
import subprocess
from sys import platform

# How many days ago to delete?
DAYS_AGO = 5

if platform == "linux":
    print("Linux")
elif platform == "win32":
    print("Windows")

windows_rmdir = r"rmdir /Q /s " # remove directory and contents without confirmation
linux_rm = "rm -r " # worst command invented ever

print("Today: ", date.today())

today = date.today()
delta = relativedelta(days=-DAYS_AGO)
number_days_ago = today + delta  # date that is DAYS_AGO from today

print(DAYS_AGO,  "Days ago: ", number_days_ago)

file_year = number_days_ago.strftime('%Y')
file_month = number_days_ago.strftime('%m')
file_day = number_days_ago.strftime('%d')

windows_base_path = "C:\\Users\\[username]\\Desktop\\scripts\\test_dir\\"
linux_base_path = "/mnt/user/camera/frontdoor/"

linux_final_path = linux_base_path + file_year + "/" + file_month + "/" + file_day
linux_final_command = linux_rm + linux_final_path

windows_final_path = windows_base_path + file_year + "\\" + file_month + "\\" + file_day
windows_final_command = windows_rmdir + windows_final_path

if platform == "win32":
    print("Is Windows directory valid? ", os.path.isdir(windows_final_path))
    if (os.path.exists(windows_final_path)):
        print("Removing directory", windows_final_path)
        subprocess.call(windows_final_command, shell=True)
    else:
        print("Opps! No directory exists")
elif platform == "linux":
    print("Is Linux directory valid? ", os.path.isdir(linux_final_path))
    if (os.path.exists(linux_final_path)):
        print("Linux final command:", linux_final_command)
        print("Removing directory", linux_final_path)
        subprocess.call(linux_final_command, shell=True)
    else:
        print("Opps! No directory exists")
