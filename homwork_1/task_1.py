duration = int(input("Введите промежуток времени в секундах: "))

second = duration % 60
minute = (duration % 3600) // 60
hour = (duration % 86400) // 3600
day = duration // 86400

if duration < 60:
    print(str(duration) + " сек")
elif duration < 3600:
    print(str(minute) + " мин " + str(second) + " сек")
elif duration < 86400:
    print(str(hour) + ' час ' + str(minute) + ' мин ' + str(second) + ' сек')
else:
    print(str(day) + ' дн ' + str(hour) + ' час ' + str(minute) + ' мин ' + str(second) + ' сек')









