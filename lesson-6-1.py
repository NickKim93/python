result = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        my_line = line.split()
        result.append((my_line[0], my_line[5].strip('"'), my_line[6]))
print(result)
