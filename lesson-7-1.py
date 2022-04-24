import os.path

print(__file__)
root = os.path.dirname(__file__)
dir_name = 'my_project'
sub_fold_list = ('settings', 'mainapp', 'adminapp', 'authapp')

for path_items in sub_fold_list:
    os.makedirs(os.path.join(dir_name, path_items), exist_ok=True)
