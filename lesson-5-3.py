tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '9В']

def my_func():
    for i in range(len(tutors)):
        try:
            yield tutors[i], klasses[i]
        except IndexError:
            yield tutors[i], None


print(my_func())
nums = my_func()
print(next(nums))
print(next(nums))
print(next(nums))
