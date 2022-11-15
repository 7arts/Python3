import  sys

with open('users.csv', 'r', encoding='utf-8') as f1, \
        open('hobby.csv', 'r', encoding='utf-8') as f2, \
        open('users_hobby.csv', 'w', encoding='utf-8') as f3:
    for user in f1:
        hobby = f2.readline().strip()
        if not hobby:
            hobby = None
        f3.write(f'{user.strip().replace(","," ")}: {hobby.replace(","," ")}\n')
    content = f2.readline()
    if content:
        sys.exit(1)
