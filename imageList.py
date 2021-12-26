
import os, sys

dir_path = "C:/Users/21622/PycharmProjects/Nouveau dossier/thumbnails/thumbnails/0/"
dirs = os.listdir( dir_path )
for lines in dirs:
    path=dir_path+lines
    with open('output.txt', 'a') as the_file:
        the_file.write(path+'\n')


