names_of_people = ["Мария", "Иван", "Маня", "Илья", "Петр"]
new_dic_names = {}
def thesaurus(args):
    for i in args:
        new_dic_names[i[0]] = [ ]  #Добавляем в словарь пару: ключ-значение
        #print(new_dic_names)
    for i in args:
        new_dic_names[i[0]].append(i)  #Добавляем значения в список к нужному ключу
        #print(new_dic_names)
    return new_dic_names
print(thesaurus(names_of_people))