import os
import re


def rename_files(directory, pattern, newname):
    files = os.listdir(directory)
    counter = 0
    for file in files:
        if re.match(pattern, file):
            filetype = file.split('.')[-1]
            os.rename(directory + '/' + file,
                      directory + '/' + newname + str(counter) + '.' + filetype)

            print('Renaming ' + file + ' to ' + newname + str(counter) + '.' + filetype)
            counter = +1


rename_files('E:\\for_Web\\питон_всякое\\file_renaming\\test','', 'my_newname')