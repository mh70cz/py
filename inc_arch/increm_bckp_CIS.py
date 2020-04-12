"""CRUD files"""
import os
import datetime as dt
import shutil

SIZE_LIMIT_DEFAULT = 64_000_000

size_limit = SIZE_LIMIT_DEFAULT
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

rootFolders_CIS_NB = [
    r"C:\Users\m.houska\Documents\_CIS",
    r"C:\Users\m.houska\Documents\_mh",
    r"C:\Users\m.houska\Documents\_notes",
    r"C:\Users\m.houska\Documents\English",
    r"C:\Users\m.houska\Documents\Templates",
    r"C:\Users\m.houska\Documents\SQL Server Management Studio",
    r"C:\Users\m.houska\Documents\Visual Studio 2015\Projects",
]
backup_folder_CIS_NB = r"C:\Users\m.houska\OneDrive\ZZ-Archive\CIS_increm"


# OnDrive from CIS NB
rootFolders_oneD = [
    r"C:\Users\m.houska\OneDrive\Documents",
    r"C:\Users\m.houska\OneDrive\Pictures",
    r"C:\Users\m.houska\OneDrive\RStudio",
    r"C:\Users\m.houska\OneDrive\scripts",
    r"C:\Users\m.houska\OneDrive\txt",
    r"C:\Users\m.houska\OneDrive - Creditinfo Solutions, s.r.o",
]
backup_folder_oneD = r"C:\Users\m.houska\OneDrive\ZZ-Archive\OneDrive_increm"


# M:
rootFolders_M = [
    r"m:\Projects\CZ_Toyota\Projects",
    r"m:\Projects\SK_Toyota\Projects",
    r"m:\Projects\CZ_Toyota\CNAV",
]
backup_folder_M = r"C:\Users\m.houska\OneDrive\ZZ-Archive\MDrive_increm"

folder_logs = r"c:\tmp\logs"
backup_folder_logs = r"C:\Users\m.houska\OneDrive\ZZ-Archive\logs"

ignored_filenames = ["Thumbs.db", "mh_tmp.txt", "mh_wrk.txt"]
ignored_extension = ["tmp", "wrk", "bak"]
delta_days = 100

now = dt.datetime.now()
before = now - dt.timedelta(days=delta_days)

error_log = []
copy_log = []
size_counter = 0
file_counter = 0


def haf():

    do_bck(rootFolders_oneD, backup_folder_oneD)
    do_bck(rootFolders_CIS_NB, backup_folder_CIS_NB)
    do_bck(rootFolders_M, backup_folder_M, 12_000_000)

    for msg in error_log:
        pass
        print(msg)

    copy_log.append(
        "*****************\n"
        f"Total files count / Total files size: {file_counter} / {size_counter}"
    )

    save_and_backup_logs(folder_logs, backup_folder_logs)


def save_and_backup_logs(folder_logs, backup_folder_logs):

    error_log_path = (
        folder_logs + "\\" + "error_log_" + now.strftime("%Y-%m-%d") + ".txt"
    )
    copy_log_path = folder_logs + "\\" + "copy_log_" + now.strftime("%Y-%m-%d") + ".txt"

    if not os.path.exists(folder_logs):
        os.makedirs(folder_logs)

    with open(error_log_path, "w") as f:
        f.write("\n".join(error_log))

    with open(copy_log_path, "w") as f:
        f.write("\n".join(copy_log))

    if not os.path.exists(backup_folder_logs):
        os.makedirs(backup_folder_logs)

    log_paths = [error_log_path, copy_log_path]
    for path in log_paths:
        dst_path = backup_folder_logs + "\\" + os.path.basename(path)
        try:
            shutil.copy2(path, dst_path)
            pass
        except Exception as e:
            msg = "some problem ({0}) with: {1} ".format(e.args[1], path)
            print(msg)


def do_bck(rootFolders, backup_folder, size_limit=SIZE_LIMIT_DEFAULT):

    """ perform backup"""
    global size_counter, file_counter
    for rootFold in rootFolders:
        for folderName, subfolders, filenames in os.walk(rootFold):
            at_least_once_passed = False  # ie file copied
            folder_size_counter = 0
            folder_file_counter = 0

            dst_path_prefix = (
                backup_folder
                + "\\"
                + now.strftime("%Y-%m-%d")
                + "-"
                + str(delta_days)
                + "_"
                + rootFold[0:1]
            )
            # + "_" #+ os.path.basename(folderName)

            for subfolder in subfolders:  # pylint: disable=unused-variable
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
                extension = extension[1:]  # remove leading "."
                if extension in ignored_extension:
                    continue

                path = folderName + "\\" + filename

                timeModiTimeStamp = os.path.getmtime(path)
                mod_time = dt.datetime.fromtimestamp(timeModiTimeStamp)
                if mod_time < before:
                    # print(filename + " modi:" + str(mod_time) + " before ")
                    pass
                else:

                    # Get the size (in bytes)
                    try:
                        size = os.path.getsize(path)
                    except OSError:
                        error_log.append(
                            "Path '%s' does not exists or is inaccessible" % path
                        )
                        continue

                    if size > size_limit:
                        msg = "file {0} is to big ({1})  ".format(path, size)
                        # print(msg)
                        error_log.append(msg)
                        continue
                    dst_path = dst_path_prefix + path.replace(
                        os.path.dirname(rootFold), ""
                    )
                    # copy_log.append(dst_path)
                    dst_folder = os.path.dirname(dst_path)
                    if not os.path.exists(dst_folder):
                        os.makedirs(dst_folder)
                    try:
                        shutil.copy2(path, dst_path)
                        # import time; time.sleep(0.05)
                        pass
                    except Exception as e:
                        msg = "some problem ({0}) with: {1} ".format(e.args[1], path)
                        error_log.append(msg)
                        # print(msg)
                    else:
                        if not at_least_once_passed:  # first passed
                            at_least_once_passed = True
                            cf_name = "The current folder is " + folderName
                            print(cf_name)
                            copy_log.append(cf_name)
                        folder_size_counter += size
                        folder_file_counter = folder_file_counter + 1
                        size_counter += size
                        file_counter += 1
                        copy_log.append(
                            filename + " modi: " + str(mod_time) + " size: " + str(size)
                        )
                        print(
                            f"Folder files count / Folder files size: "
                            f"{folder_file_counter} / {folder_size_counter} \r",
                            end="",
                        )
            if at_least_once_passed:
                print(
                    f"Folder files count / Folder files size: "
                    f"{folder_file_counter} / {folder_size_counter}",
                    f"  * Total file count / Total files size: "
                    f"{file_counter} / {size_counter}",
                )


haf()
