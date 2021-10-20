def type_logger(func):
    def wrapper(*args):
        for arg in args:
            x_type = type(arg)
            print(f'{arg}: {x_type}', end=', ')
        return func(*args)
    return wrapper

@type_logger
def calc_square(*args):
    return list(map(lambda x: x * 2, args))

a = calc_square(2, 3, 4)
print(a)
b = calc_square('qwe', 5)
print(b)
c = calc_square(2.2, 2, 4.4)
