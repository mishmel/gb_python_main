def thesaurus(name):
    first_letter = []
    same_names = {}
    for i in name:
        if not i[0] in first_letter:
            first_letter.append(i[0])
            same_names[i[0]] = [i]
        else:
            a = same_names.setdefault(i[0], i)
            a.append(i)
    return same_names
    #если потребуется сортировка по ключам:
    #return:sorted(same_names.items())

print(thesaurus(['Михаил', 'Ангелина', 'Алексей', 'Максим', 'Василиса', 'Ольга', 'Антон', 'Иннокентий', 'Иван']))

