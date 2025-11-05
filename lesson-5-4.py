src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [elem for index, elem in enumerate(src) if elem > src[index - 1] and index != 0]
print(result)
