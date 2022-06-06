import os
from random import randint, random
import shutil

filter_dir = input("Folder to filter : ")
store_dir = input("Folder to move in : ")

def recurse(the_path) : 
    path_to_check = the_path
    
    for items in os.listdir(the_path) : 
        
        if os.path.isdir(path_to_check + items) :
            recurse(path_to_check + items + "/")
        else :
            if items.endswith(".txt") or items.endswith(".rtf") : #change the type of file extensions to whatever you want
                
                name, extension = os.path.splitext((path_to_check + items))
                randname = name + str(randint(0,99999999)) + extension
                cleanedname = randname.rsplit("/", 1)
                
                try :
                    
                    os.rename((path_to_check + items), randname)
                    shutil.move(randname, store_dir + str(cleanedname[1]))
                    
                except Exception:
                    
                    pass

recurse(filter_dir)
print("done")
