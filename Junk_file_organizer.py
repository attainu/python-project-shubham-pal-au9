import argparse
import os
import shutil
from datetime import datetime
import time
from stat import ST_SIZE


class JunkFileOrganizer:

    def __init__(self):
        pass

    def get_Data(self, path, file_Data):
        for file in os.scandir(path):
            if not file.is_dir():
                fileName = file.name
                filePath = file.path
                fileExtension = fileName.split('.')[-1]
                fileSize = os.stat(filePath)[ST_SIZE]
                temp = [fileName, filePath, fileExtension, fileSize]
                file_Data.append(temp)
            else:
                info = (self.get_Data(file.path, file_Data))
                file_Data + [data for data in info]

        return file_Data

    # Function to arrange the file according to their extension

    def organize_by_extension(self, path, files_Data, organizedPath):
        for data in files_Data:
            fileName = data[0]
            filePath = data[1]
            extension = data[2]

            if not os.path.exists(organizedPath + extension):
                os.makedirs(organizedPath + extension)

            shutil.move(filePath, organizedPath + extension + '/' + fileName)

    # Function to arrange the files according their size

    def organize_by_size(self, path, files_Data, organizedPath):
        for data in files_Data:
            fileName = data[0]
            filePath = data[1]
            size = data[3]
            if 0 <= size < 1000:  # bytes
                if not os.path.exists(organizedPath + 'Bytes'):
                    os.makedirs(organizedPath + 'Bytes')

                shutil.move(filePath, organizedPath + 'Bytes/' + fileName)

            elif 1000 < size < 1000000:
                if not os.path.exists(organizedPath + 'KiloBytes'):
                    os.makedirs(organizedPath + 'KiloBytes')

                shutil.move(filePath, organizedPath + 'KiloBytes/' + fileName)

            elif 1000000 < size < 100000000:
                if not os.path.exists(organizedPath + 'MegaBytes'):
                    os.makedirs(organizedPath + 'MegaBytes')

                shutil.move(filePath, organizedPath + 'MegaBytes/' + fileName)

            # If any file larger than 100 MB
            else:
                if not os.path.exists(organizedPath + 'Greater than 100MB'):
                    os.makedirs(organizedPath + 'Greater than 100MB')

                shutil.move(filePath, organizedPath + 'Greater than 100MB/' +
                            fileName)

    # Function arrange the files by their last modified date

    def organize_by_date(self, path, files_Data, organizedPath):

        name = os.listdir(path)
        name.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
        files = [f for f in name if os.path.isfile(os.path.join(path, f))]

        os.chdir(path)

        for x in files:

            # Get the creation time of file and
            # make folder of it to store files

            create_time = time.ctime(os.path.getmtime(os.path.join(path, x)))
            create_dt = datetime.strptime(create_time, '%a %b %d %H:%M:%S %Y')
            modified_date = str(create_dt.day) + '-' + str(
                            create_dt.month) + '-' + str(create_dt.year)

            if(os.path.isdir(organizedPath + modified_date)):
                shutil.move(os.path.join(path, x), organizedPath + modified_date)

            else:
                os.makedirs(organizedPath + modified_date)
                shutil.move(os.path.join(path, x), organizedPath + modified_date)

    # Function to delete the organize folder
    def delete_dir(self, path, files_Data, organizedPath):
        if os.path.isdir(organizedPath):
            shutil.rmtree(organizedPath)

    # Create organize folder if it is not exists
    def organize(self, args):
        path = args.d
        organizeBy = args.o

        # Prevent from error during wrong path input
        try:
            files_Data = self.get_Data(path, [])
        except FileNotFoundError:
            print('Invalid path of directory')
            return

        if not os.path.exists(path + '/organized'):
            os.makedirs(path + '/organized')

        organizedPath = path + '/organized/'

        if organizeBy == 'ext':
            self.organize_by_extension(path, files_Data, organizedPath)
            print('Organized by Extention Completed')
            print('Please check folder: '+path)

        elif organizeBy == 'size':
            self.organize_by_size(path, files_Data, organizedPath)
            print('Organized by Size Completed')
            print('Please check folder: '+path)
        elif organizeBy == 'date':
            self.organize_by_date(path, files_Data, organizedPath)
            print('Organized by Modified Date of File  Completed')
            print('Please check folder: '+path)
        elif organizeBy == 'delete':
            self.delete_dir(path, files_Data, organizedPath)


# Driver code
if __name__ == '__main__':

    parameter = argparse.ArgumentParser()
    # Take path and option from user through command line argument
    parameter.add_argument('-d', default='D:\\New', help='path to organize')
    parameter.add_argument('-o', default='ext', help='Organize by',
                           choices=['ext', 'size', 'date', 'delete'])

    args = parameter.parse_args()
    obj_junk = JunkFileOrganizer()
    obj_junk.organize(args)
