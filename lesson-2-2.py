#task 2
list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_1.insert(1, '"')
list_1.insert(3, '"')
list_1.insert(5, '"')
list_1.insert(7, '"')
list_1.insert(12, '"')
list_1.insert(14, '"')
list_1[2] = '05'
list_1[13] = '+05'
print(list_1)
string_1 = ''.join(list_1[0]) + ' ' + ''.join([list_1[i] for i in [1, 2, 3]]) + ' ' + ''.join(list_1[4]) + ' ' + ''.join([list_1[i] for i in [5, 6, 7]]) + ' ' + ' '.join([list_1[i] for i in [8, 9, 10, 11]]) + ' ' + ''.join([list_1[i] for i in [12, 13, 14]]) + ' ' + ''.join(list_1[15])
print(string_1) # Код уродливый и простой, пытался его упорядочить и привести в нормальный вид в следующей задаче.