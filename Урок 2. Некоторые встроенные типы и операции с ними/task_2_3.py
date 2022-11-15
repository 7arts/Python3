my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#list_1 = len(my_list)
#print(list_1)
for i in range(len(my_list)):
    ind = my_list.pop(0)
    #print(ind)
    if ind.isdigit():
        my_list.append(f'"{int(ind):02d}"')
    elif ind[0] == '+' and ind[1].isdigit():
        my_list.append(f'"+{int(ind):02d}"')
    else:
        my_list.append(ind)
print(' '.join(my_list))
