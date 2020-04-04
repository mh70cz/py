"""CRUD files on Linux"""
import os
import datetime as dt
import shutil

exclude_folder_names = []
exclude_file_names = []
exclude_file_extensions = []
now = dt.datetime.now()
delta_days = 100
before = now - dt.timedelta(days=delta_days)

error_log = []

def main():


    rootFolders = [
        r"/home/irena/Documents",
        r"/home/irena/Pictures",
        r"/home/mh/test"
    ]
    print_details = False
    copy_files = True
    dst_path_prefix = "/tmp/irena"
    

    iterate_over_files(rootFolders, print_details, dst_path_prefix, copy_files)

def iterate_over_files(rootFolders, print_details, dst_path_prefix, copy_files):
    """ iterarate over files"""
    grand_total_size = 0
    grand_file_count = 0
    for rootFolder in rootFolders:
        root_folder_size = 0
        root_file_count = 0
        for folderName, subfolders, filenames in os.walk(rootFolder):
            if folderName in exclude_folder_names:
                continue

            folder_total_size = 0
            folder_file_count = 0

            for filename in filenames:                
                if excludedFilenameOrExtension(filename):
                    continue
                path = folderName + "/" + filename
                timeModiTimeStamp = os.path.getmtime(path)
                mod_time = dt.datetime.fromtimestamp(timeModiTimeStamp)
                if mod_time  < before:
                    continue
                
                dst_path = dst_path_prefix + path.replace(
                        os.path.dirname(rootFolder), "")
                if print_details:
                    print(dst_path + " " + str(mod_time))
                
                if copy_files:
                    dst_folder = os.path.dirname(dst_path)
                    if not os.path.exists(dst_folder):
                        os.makedirs(dst_folder)
                    try:
                        shutil.copy2(path, dst_path)
                    except(PermissionError):
                        print("PermissionError " + path)
                
                size = os.path.getsize(path)
                folder_file_count += 1
                folder_total_size += size
            if print_details:
                print("folder: {0}   file count: {1:,}   size:   {2:,}"
                    .format(folderName, folder_file_count, folder_total_size))

            root_file_count += folder_file_count
            root_folder_size += folder_total_size              
        print("root folder: {0}   file count: {1:,}  size: {2:,}"
              .format(rootFolder, root_file_count, root_folder_size))

        grand_file_count += root_file_count
        grand_total_size += root_folder_size
    print("Grand total file count: {0:,}   Grand total file size: {1:,}"
          .format(grand_file_count, grand_total_size))

    def innerLoop():
        pass

def excludedFilenameOrExtension(filename):
    """return True if filename or file extension is in excluded list"""
    if filename in exclude_file_names:
        return True
    extension = os.path.splitext(filename)[-1].lower()
    # splits filename to a name and an extension (extension includes leading ".")
    # This method ignores leading periods so ".mp3" is not considered an mp3 file.
    # This is however the way a leading period should be treated.
    # E.g .gitignore is not a file format
    extension = extension[1:]
    if extension in exclude_file_extensions:
        return True


if __name__ == "__main__":
    main()
