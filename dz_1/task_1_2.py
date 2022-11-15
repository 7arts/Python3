cub = []
num = 1
while num < 1000:
    if num % 2:
        cub.append(num ** 3)
        num = num + 1
    else:
        num = num + 1

all_sum = 0

for i, val in enumerate(cub):
    sum = 0
    while val > 0:
        sum = sum + val % 10
        val = val // 10
    if sum % 7 == 0:
        all_sum = all_sum + cub[i]
print(all_sum)

cub_17 = []
all_sum_1 = 0
for x in cub:
    cub_17.append(x+17)

for i, val in enumerate(cub_17):
    sum = 0
    while val > 0:
        sum = sum + val % 10
        val = val // 10
    if sum % 7 == 0:
        all_sum_1 = all_sum_1 + cub_17[i]
print(all_sum_1)


