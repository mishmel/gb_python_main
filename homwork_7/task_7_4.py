import os

files = []
for r, d, f in os.walk('../'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)

max_size = max(files)
#print(max_size)
info = {}
i = 1
for _ in range(len(str(max_size))):
    i *= 10
    info[i] = 0
#print(info)
for file in files:
    info[10 ** len(str(file))] += 1
print(info)
