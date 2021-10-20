import sys

num = sys.argv[1:]

with open('bakery.csv', encoding='utf-8') as f:
    if len(num) > 1:
        starting_index = int(num[0])
        end_index = int(num[1])
    elif len(num) == 0:
        starting_index = 0
        end_index = sum(1 for line in f)
        f.seek(0)
    else:
        starting_index = int(num[0])
        end_index = sum(1 for line in f)
        f.seek(0)

    for ind, val in enumerate(f):
        if starting_index <= ind + 1 <= end_index:
            print(val.strip())