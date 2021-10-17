import os
sample = {'my_project' : ['setting', 'mainnapp', 'adminapp', 'authapp']}
for root, folders in sample.items():
    if os.path.exists(root):
        print('папка существует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)
