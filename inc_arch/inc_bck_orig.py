'''CRUD files'''
import os
import datetime as dt
import shutil


# rootFolders_home = [
#     r"C:\Users\Miroslav\Documents\_MiraHxf",
#     r"C:\Users\Miroslav\Documents\_Byt",
#     r"C:\Users\Miroslav\Documents\_notes",
#     r"C:\Users\Miroslav\Documents\certificates",
#     r"C:\Users\Miroslav\Documents\Snagit",
#     r"C:\Users\Miroslav\Documents\web",
#     r"C:\Users\Miroslav\Pictures",
#     r"D:\Data\Foto",
#     r"D:\Data\Pictures",
#     r"D:\Data\web"
#     ]
# backup_folder = r"C:\Users\Miroslav\OneDrive\ZZ_BackupHome"

  # CIS
rootFolders_oneD = [
    r"C:\Users\m.houska\Documents\_CIS",
    r"C:\Users\m.houska\Documents\_mh",
    r"C:\Users\m.houska\Documents\_notes",
    r"C:\Users\m.houska\Documents\English",
    r"C:\Users\m.houska\Documents\Templates",
    r"C:\Users\m.houska\Documents\SQL Server Management Studio",
    r"C:\Users\m.houska\Documents\Visual Studio 2015\Projects"
    ]
backup_folder_oneD = r"C:\Users\m.houska\OneDrive\ZZ-Archive\CIS_increm"

#OnDrive from CIS NB
rootFolders_CIS_NB = [
    r"C:\Users\m.houska\OneDrive\Documents",
    r"C:\Users\m.houska\OneDrive\Pictures",
    r"C:\Users\m.houska\OneDrive\RStudio",
    r"C:\Users\m.houska\OneDrive\scripts",
    r"C:\Users\m.houska\OneDrive\txt"
    ]
backup_folder_CIS_NB = r"C:\Users\m.houska\OneDrive\ZZ-Archive\OneDrive"


ignored_filenames = ["Thumbs.db"]
ignored_extension = ["tmp", "wrk"]
delta_days = 100
now = dt.datetime.now()
before = now - dt.timedelta(days=delta_days)

def haf():
    do_bck(rootFolders_oneD, backup_folder_oneD)
    do_bck(rootFolders_CIS_NB, backup_folder_CIS_NB)

def do_bck(rootFolders, backup_folder):

    """ perform backup"""
    for rootFold in rootFolders:
        for folderName, subfolders, filenames in os.walk(rootFold):
            #print("The current folder is " + folderName)
            loop_passed = False
            dst_path_prefix = backup_folder + "\\" + now.strftime("%Y-%m-%d") + \
                "-" + str(delta_days) + "_" + rootFold[0:1]
            # + "_" #+ os.path.basename(folderName)

            for subfolder in subfolders:
                # print("Subfolder of " + folderName + ": " + subfolder)
                pass
            for filename in filenames:
                if filename in ignored_filenames:
                    continue
                extension = os.path.splitext(filename)[-1].lower()
                # splits filename to a name and an extension (extension includes leading ".")
                # This method ignores leading periods so ".mp3" is not considered an mp3 file.
                # This is however the way a leading period should be treated.
                # E.g .gitignore is not a file format
                extension = extension[1:] # remove leading "."
                if extension in ignored_extension:
                    continue

                path = folderName + "\\" + filename
                timeModiTimeStamp = os.path.getmtime(path)
                mod_time = dt.datetime.fromtimestamp(timeModiTimeStamp)
                if mod_time < before:
                    #print(filename + " modi:" + str(mod_time) + " before ")
                    pass
                else:
                    if not loop_passed:
                        print("")
                        print("The current folder is " + folderName)
                        loop_passed = True
                    print(filename + " modi: " + str(mod_time) + " after ")
                    dst_path = dst_path_prefix + path.replace(os.path.dirname(rootFold), "")
                    print(dst_path)
                    dst_folder = os.path.dirname(dst_path)
                    if not os.path.exists(dst_folder):
                        os.makedirs(dst_folder)
                    shutil.copy2(path, dst_path)

haf()

