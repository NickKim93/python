import os
import shutil

source_dir = os.path.join(os.path.dirname(__file__), 'my_project')
destination_dir = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

for root_dir_path, sub_dirs, file_names in os.walk(source_dir):
    if root_dir_path.count('templates'):
        for dirs in sub_dirs:
            if not os.path.exists(os.path.join(destination_dir, dirs)):
                os.makedirs(os.path.join(destination_dir, dirs))
        for file in file_names:
            source = os.path.join(root_dir_path, file)
            destination = os.path.join(destination_dir, os.path.basename(root_dir_path))
            print(destination)
            if not os.path.dirname(source) == destination:
                shutil.copy(source, destination)
                print('copied', file_names)
