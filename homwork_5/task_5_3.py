from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def tutor_klasse():

    for i in zip_longest(tutors, klasses[0:len(tutors)], fillvalue='None'):
        yield i

tutors_klasses = tutor_klasse()

print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))
print(next(tutors_klasses))


