def type_logger(original_func):
    def wrapper(*args):
        res_type = original_func(*args)
        for arg in args:
            print(f'{arg}: {type(arg)}')
        return res_type
    return wrapper


@type_logger
def calc_cube(x, *args):
    return x ** 3


a = calc_cube(5, 6, 7)
print(a)
