employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in employees:
    employee = i.split(' ')
    print('Привет, ' + employee[-1].title() + '!')


