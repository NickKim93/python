from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    input_arg = len(argv)
    if input_arg == 1:
        print(f.readlines())
    elif input_arg == 2:
        for line in f.readlines()[int(argv[1]) - 1:]:
            print(line, end='')
    elif input_arg == 3:
        for line in f.readlines()[int(argv[1]) - 1: int(argv[2])]:
            print(line, end='')
