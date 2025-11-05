#task 3
def thesarius(*args):
    dict_names = dict()
    for elem in args:
        if elem[0] in dict_names:
            dict_names[elem[0]].append(elem)
        else:
            dict_names[elem[0]] = [elem]
    print(dict_names)


thesarius('Игорь', 'Мария', 'Петр', 'Илья')