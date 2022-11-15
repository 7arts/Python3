tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

#result = ((i, j) for i,j in zip(tutors, klasses) if len(tutors) > len(klasses) )


def result():
    j = len(klasses)
    for i, tut in enumerate(tutors):
        if i < j:
            yield tut, klasses[i]
        else:
            yield tut, None


print(*result())