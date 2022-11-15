price = [65, 45.52, 69, 12, 5, 32.04, 78, 96.3, 98, 34, 68.96, 35]
obj = id(price)
print(obj)
price.sort()
print(price)
job = id(price)
print(job)
new_list = sorted(price, reverse = True)
print(new_list)

for i, num in enumerate(price):
    price_1 = (f"{num:.2f}").split(".")
    #print(price_1)
    pr_a = (f"{price_1[0]} руб {price_1[1]} коп") #end= ', ')
    print(pr_a, end= ', ')
print('.')
for j, nums in enumerate(new_list[:5][::-1]):
        price_2 = (f"{nums:.2f}").split(".")
        #print(price_1)
        pr_a_1 = (f"{price_2[0]} руб {price_2[1]} коп") #end= ', ')
        print(pr_a_1, end= ', ')







