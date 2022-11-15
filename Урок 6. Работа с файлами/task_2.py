dp = {}
with open('nginx_logs.txt', "r", encoding="utf-8") as f:
    for line in f:
        ad = line.split(" - - ")[0]
        if ad not in dp:
            dp[ad] = 1
        else:
            dp[ad] += 1
print(dp)
print(max(dp, key=dp.get))
print(dp.get(max(dp, key=dp.get)))
