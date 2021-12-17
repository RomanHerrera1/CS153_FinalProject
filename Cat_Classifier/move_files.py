import os
import shutil

source_path = "/Users/romanherrera/Desktop/Computer_Vision/Project/archive/raw-img/"
foldernames = os.listdir(source_path)

# Loops through all folders in a given path and separates them into traning and validation folders

# for folder in foldernames:
#     if folder == '.DS_Store':
#         continue

#     dest_train = "/Users/romanherrera/Desktop/Computer_Vision/Project/Imgs/training/neither/"
#     d est_validation = "/Users/romanherrera/Desktop/Computer_Vision/Project/Imgs/validation/neither/"
#     # dest = "/Users/romanherrera/Desktop/Computer_Vision/Project/archive/raw-img/butterfly/"
    
#     source = source_path + folder + "/"
#     files = os.listdir(source)

#     num_files = len(files)
#     for k, f in enumerate(files):
#         if not k % 9 == 0:
#             shutil.move(source+f, dest)

        # Used to take 1/9th of each non-cat category and split it 1/3 validation and 2/3 training
        # if k % 9 == 0:
        #     if k % 27 == 0:
        #         shutil.move(source+f, dest_validation)
        #     else:
        #         shutil.move(source+f, dest_train)
            

# Useful for just one folder to another
dest_train = "/Users/romanherrera/Desktop/Computer_Vision/Project/Imgs/training/artificial_cat/"
dest_validation = "/Users/romanherrera/Desktop/Computer_Vision/Project/Imgs/validation/artificial_cat/"
source = "/Users/romanherrera/Desktop/Computer_Vision/Project/Imgs/artificial_cats/"
files = os.listdir(source)
num_files = len(files)
print(num_files)
for k, f in enumerate(files):
    # shutil.move(dest_validation+f, source)
    if k % 3 == 0:
        shutil.move(source+f, dest_validation)
    else:
        shutil.move(source+f, dest_train)

