#task 2
def num_translate(x):
    my_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
               'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if x.istitle():
        my_dict = {k.title(): v.title() for k, v in my_dict.items()}
    return my_dict.get(x, None)

print(num_translate(input('Введите число от 0 до 10 на английском: ')))
