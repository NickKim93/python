# 1

def odd_nums(max_num):
    for x in range(1, max_num + 1):
        if x % 2 != 0:
            yield x


nums = odd_nums(15)
print(next(nums))
print(next(nums))
print(next(nums))