import os
import shutil

sample = {'my_project':
    [{'setting': ['__init__.py', 'dev.py', 'prog.py'
    ],
    },
     {'mainapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
         'mainapp': ['base.html', 'index.html']}]
     }]},
     {'authapp': ['__init.py', 'models.py', 'views.py', {'templates': [{
         'authapp': ['base.html', 'index.html']}]
     }
                   ]
      }
    ]
}
def creat_data(data):
    for folder, data_tmps in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for data_tmp in data_tmps:
            if isinstance(data_tmp, dict):
                creat_data(data_tmp)
            else:
                if not os.path.exists(data_tmp):
                    if '.' in data_tmp:
                        with open(data_tmp, 'w') as f:
                            f.write('')
    else:
        os.chdir('../')

creat_data(sample)

my_dir = 'task_3'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'
files = []

for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
#print(files)

for path in files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)
