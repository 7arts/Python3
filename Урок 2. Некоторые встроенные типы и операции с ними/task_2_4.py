my_list = ['инженер-конструктор Игорь','главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй','директор аэлита']
for my_str in my_list:
    name = my_str.split()[-1]
    print(f'Привет, {name.capitalize()}!')