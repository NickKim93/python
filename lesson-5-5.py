src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = set()
repeated_nums = set()

for num in src:
    if num in repeated_nums:
        continue
    if num in result:
        result.discard(num)
        repeated_nums.add(num)
        continue
    else:
        result.add(num)

print([num for num in src if num in result])
