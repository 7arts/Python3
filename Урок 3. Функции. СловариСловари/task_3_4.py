names_of_people = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",]
new_dic_names = {}
def thesaurus_adv(args):
    for i in args:
        a, b = i.split()
        if new_dic_names.get(b[0]) == None:
            #print(b[0])
            new_dic_names[b[0]] = {a[0] : [i]}
            #print(new_dic_names)
        elif new_dic_names[b[0]].get(a[0]) == None:
            #print(a[0])
            new_dic_names[b[0]][a[0]] = [i]
            #print(new_dic_names)
        else:
            new_dic_names[b[0]][a[0]].append(i)
            #print(new_dic_names)

    return new_dic_names
print(thesaurus_adv(names_of_people))

