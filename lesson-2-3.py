list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(list_1) - 1):
    if list_1[i] == list_1[i + 1]:
        print(i)
        continue
    else:
        if list_1[i].isdigit() or list_1[i].startswith('+'):
            list_1.insert(i + 1, '"')
print(list_1)

for element in list_1:
    if element.isdigit() or element.startswith('+'):
        list_1.insert(list_1.index(element) + 1, '"')
for element in list_1:
    if element.isdigit() or element.startswith('+'):
        list_1.insert(list_1.index(element), '"')
        break
print(list_1)
# Так и не смог до конца решить задачу. Не совсем понятно, как продолжить цикл, когда он бесконечно вставляет " перед первым попавшимся числом