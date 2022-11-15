import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#print(random.choice(nouns))
def get_jokes(n):
    i = 1
    d = []
    while i <= n:
        a = random.choice(nouns)
        #print(a)
        b = random.choice(adverbs)
        #print(b)
        c = random.choice(adjectives)
        #print(c)
        d.append(f'{a} {b} {c}')
        #print(d)
        i += 1
    return d
print(get_jokes(5))