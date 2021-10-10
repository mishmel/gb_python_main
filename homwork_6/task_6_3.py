import json
with open('users.csv', 'r', encoding='utf-8') as f:
    users = []
    for line in f:
        users.append(line.strip())

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby = []
    for line in f:
        hobby.append(line.strip())

user = {}
label_greater = len(users)
label_less = len(hobby)
for i in range(len(users)):
    if len(users) < len(hobby):
        exit(1)
    else:
        if label_less > 0:
            user.setdefault(users[i], hobby[i])
            label_less -= 1
        else:
            user.setdefault(users[i], None)

print(user)

with open('users.txt', 'w', encoding='utf-8') as f:
    json.dump(user, f, ensure_ascii=False)