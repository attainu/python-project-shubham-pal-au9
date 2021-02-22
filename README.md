## Python Project - Junk File Organizer

Junk File organizer is use to organize the files within seconds.

## Aim of Project

The aim of this project is to write a python script that organize the files on the bases of extension, size and last modified date inside organized folder.We have also incorporate here one additional function of delete that is use to delete the organize folder if it is created by mistake. 

## Python Packages and Libraries Used:
- argparse
- os 
- shutil
- datetime
- time
- stat
- ST_SIZE

## Technology Used:
- Python 3.8

## Main functionality of this project:
1. Organized by extension: By using this option user can organize their files by their file extension, create a new folder with the parent called organized which will contain all the files in organize sub folder by their extensions.
2. Organize by size: By using this option user can organize their files by their file size like KB,MB and greater than 100 MB, create a new folder with the parent called organized which will contain all the files in organize sub folder by their size.
3. Organize by date: By using this option user can organize their files by their file last modified date, create a new folder with the parent called organized which will contain all the files in organize sub folder by their last modified date.
4. Delete organize folder:
This option is use when user create organize folder by mistake so they can use this option to delete the organize folder along with their contents.

## How To Run This Project File
Organize by extension:
```bash
PS D:\AttainU\AttainU Stuff\Projects\Project_Junk_file_organiz\python-project-shubham-pal-au9> 
python Junk_file_organizer.pyd "D:\New\folder1" -o ext
```
Organize by size:
```bash
PS D:\AttainU\AttainU Stuff\Projects\Project_Junk_file_organiz\python-project-shubham-pal-au9> 
python Junk_file_organizer.pyd "D:\New\folder2" -o size
```
Organize by date:
```bash
PS D:\AttainU\AttainU Stuff\Projects\Project_Junk_file_organiz\python-project-shubham-pal-au9> 
python Junk_file_organizer.pyd "D:\New\folder3" -o date
```
Delete organize folder:
```bash
PS D:\AttainU\AttainU Stuff\Projects\Project_Junk_file_organizer\python-project-shubham-pal-au9> 
python Junk_file_organizer.py -o delete
```