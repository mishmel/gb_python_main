for i in range(1, 101):
    if i % 10 == 1 and i != 11:
        print(str(i) + ' процент')
    elif (i % 10 == 2 and i != 12) or (i % 10 == 3 and i != 13) or (i % 10 == 4 and i != 14):
        print(str(i) + ' процента')
    else:
        print(str(i) + ' процентов')

