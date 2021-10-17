def odd_nums(max_num):
    for i in range(1, max_num + 1, 2):
        yield i

odd_nums_15 = odd_nums(15)
print(next(odd_nums_15))
print(next(odd_nums_15))
print(next(odd_nums_15))
print(next(odd_nums_15))
print(next(odd_nums_15))
print(next(odd_nums_15))
print(next(odd_nums_15))
print(next(odd_nums_15))
print(next(odd_nums_15))
