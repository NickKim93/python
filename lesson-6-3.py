from itertools import zip_longest

user_init = []
user_hobby = []
my_dict = {}

with open('users.csv', 'r', encoding='utf-8') as f:
    with open('hobby.csv', 'r', encoding='utf-8') as f1:
        for line in f:
            my_line = line.split(',')
            user_init.append(my_line[2].strip('\n') + ' ' + my_line[0] + ' ' + my_line[1])
        for val in f1:
            user_hobby.append(val.strip('\n'))
        my_dict = dict(zip_longest(user_init, user_hobby[:len(user_init)], fillvalue= None))
print(my_dict)
