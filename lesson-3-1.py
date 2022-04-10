#task 1

def num_translate(x):
    my_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
               'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',  'nine': 'девять', 'ten': 'десять'}
    return my_dict.get(x, None)


print(num_translate(input('Введите число от 0 до 10 на английском: ')))
print(num_translate('zero'))