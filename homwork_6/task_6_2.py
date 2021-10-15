with open('nginx_logs.txt') as f:
    required_data = []
    spammer = {}
    for line in f:
        desired_string = line.split()
        required_data.append((desired_string[0], desired_string[5].replace('"', ''), desired_string[6]))
        spammer.setdefault(desired_string[0], 0)
        spammer[desired_string[0]] += 1

spammer = sorted(spammer.items(), key=lambda x: x[1], reverse=True)

print(spammer[:5])