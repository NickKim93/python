import os

source_dir = 'C:/Users/nikit/Music'
size_dictionary = {'100': 0, '1000': 0, '10000': 0, '100000': 0}

for dir_path, sub_dirs, files in os.walk(source_dir):
    for file in files:
        fp = os.path.join(dir_path, file)
        if os.stat(fp).st_size <= 100:
            size_dictionary['100'] += 1
        elif 1000 >= os.stat(fp).st_size >= 100:
            size_dictionary['1000'] += 1
        elif 10000 >= os.stat(fp).st_size >= 1000:
            size_dictionary['10000'] += 1
        else:
            size_dictionary['100000'] += 1
print(size_dictionary)
