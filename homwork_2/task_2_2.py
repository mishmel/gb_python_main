forecast = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

#Проверяем, есть ли не алфавитные символы в каждом элементе списка
for i in range(len(forecast)):
    new = forecast[i]
    if not forecast[i].isalpha():
        new = '"{:02d}"'.format(int(forecast[i]))
        if '+' in forecast[i]:
            new = '"+{:02d}"'.format(int(forecast[i]))
    forecast[i] = new

message = ' '.join(forecast)
print(message)




