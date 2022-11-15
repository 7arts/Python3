result = []
with open('nginx_logs.txt', "r", encoding="utf-8") as f:
    for line in f:
        ad = line.split(" - - ")[0]
        typ_and_res = line.split('"')[1]
        typ = typ_and_res.split()[0]
        res = typ_and_res.split()[1]
        result.append((ad, typ, res))
print(result)