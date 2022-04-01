# task 1
duration_seconds = int(input('Введите продолжительность в секундах: '))
minutes, seconds = divmod(duration_seconds, 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)
if days == 0:
    if hours == 0:
        print('%d мин : %d сек' % (minutes, seconds))
    print('%d час %d мин : %d сек' % (hours, minutes, seconds))
else:
    print('%d дн %d час %d мин : %d сек' % (days, hours, minutes, seconds))

# task 2

import math
uneven_numbers = []
for number in range(1, 1000, 2):
    number = int(math.pow(number, 3))
    uneven_numbers.append(number)
print(uneven_numbers)
sum = 0
for i in range(len(uneven_numbers)):
    if uneven_numbers[i] % 7 == 0:
        sum += uneven_numbers[i]
print('The sum of numbers divisible by 7 = ', sum)
uneven_numbers = list(map(lambda x: x + 17, uneven_numbers))
print(uneven_numbers)
for i in range(len(uneven_numbers)):
    if uneven_numbers[i] % 7 == 0:
        sum += uneven_numbers[i]
print('The sum of numbers divisible by 7 = ', sum)

# task 3

percent = input('Введите процентовку от 0 до 100 % : ')
last_digit = int(percent[-1])
if len(percent) <= 1:
    after_last_digit = 0
else:
    after_last_digit = int(percent[-2])
# print(last_digit)
# print(after_last_digit)
if after_last_digit == 1:
    print(percent, ' процентов')
else:
    if last_digit == 1:
         print(percent, ' процент')
    else:
        if last_digit == 2 or last_digit == 3 or last_digit == 4:
            print(percent, ' процента')
        else:
            print(percent, ' процентов')

