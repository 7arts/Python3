import re

res = re.compile(r"(?P<addres>.+)\s-\s-\s\[(?P<datatime>.+)\]\s\"(?P<resp>\w+)\s(?P<file>/\w+/\w+)\s.+\"\s(?P<code>\d+)\s(?P<size>\d+)\s")

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    content = f.read().splitlines()

for con in content:
    result = res.findall(con)
    if result:
        print(tuple(result)[0])
