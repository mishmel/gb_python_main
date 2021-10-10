from itertools import zip_longest
import json
user = {}
with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    with open('users.csv', 'r', encoding='utf-8') as users:
        with open('hobby.csv', 'r', encoding='utf-8') as hobby:
            sum_line_users = sum(1 for line in users)
            sum_line_hobby = sum(1 for line in hobby)

            if sum_line_hobby > sum_line_users:
                exit(1)

            users.seek(0)
            hobby.seek(0)

            for line_users, line_hobby in zip_longest(users, hobby):
                f.write(f'{line_users.strip()} :' f' {line_hobby.strip() if line_hobby is not None else line_hobby}\n')



