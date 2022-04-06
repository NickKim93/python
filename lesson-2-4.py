# task 4

def format_string_from_list(_str):
    return _str.strip().title().split(' ')[-1]


list_1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
new_list = [format_string_from_list(_str) for _str in list_1]
for i in range(len(new_list)):
    print('Привет, %s' % new_list[i])