# как сделал сам
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    required_data = []
    for line in f:

        line_1 = line.split(' -')
        remote_addr = line_1[0]
        line_2 = line_1[2].split('"')
        line_3 = line_2[1].split(' ')
        request_type = line_3[0]
        requested_resource = line_3[1]
        desired_string = ()
        desired_string = (remote_addr, request_type, requested_resource)
        required_data.append(desired_string)

print(required_data)

# переделал после разбора, код меньше, не заметил разницу по времени, но выглядит лучше)
with open('nginx_logs.txt') as f:
    required_data = []
    for line in f:
        desired_string = line.split()
        required_data.append((desired_string[0], desired_string[5].replace('"', ''), desired_string[6]))

print(required_data)

