import  sys
import json

result = {}
with open('users.csv', 'r', encoding='utf-8') as f1, \
        open('hobby.csv', 'r', encoding='utf-8') as f2:
    for user in f1:
        hobby = f2.readline().strip()
        if not hobby:
            hobby = None
        if user not in result:
            result[user.strip().replace(","," ")] = hobby
    content = f2.read()
    if content:
        sys.exit(1)
print(result)

with open('res.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False)
with open('res.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
print(res)