price_list = [3.7, 77, 1.25, 33, 11, 11.11, 25, 44.4, 97, 57.8, 1]

#Создаём список цен нужного нам вида(скорее всего надо было делать
#через форматирование, но я пока додумался только так)
beautiful_price = []

for i in range(len(price_list)):
    price_product = str(price_list[i])
    split_price = price_product.split('.')
    k = []
    if len(split_price) > 1:
        for i in split_price:
            i = int(i)
            k.append(i)
        designations = '{0:2d}руб {1:02d}коп,'.format(k[0], k[1])
        beautiful_price.append(designations)
    else:
        i = int(split_price[0])
        k.append(i)
        designations = '{0:2d}руб,'.format(k[0])
        beautiful_price.append(designations)

#Выводим цены через запятую в одну строку в заданном виде
message = ' '.join(beautiful_price)
print(message)

#Отсортированный список по возрастанию цены(id одинаковые)
print(id(beautiful_price))
print(sorted(beautiful_price))
print(id(beautiful_price))

#Отсортированный список по убыванию цены
a = sorted(beautiful_price)
print(a[::-1])

#Срез 5-ти самых дорогих цен
print(a[::-1][:5])

#Долго делал, скорее всего это всё можно сделать проще и более приятного вида



