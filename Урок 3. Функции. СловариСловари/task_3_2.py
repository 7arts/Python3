dictionary = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четире",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
}

def num_translate(dic, word):
    if word.istitle():
        a = word.lower()
        b = dic.get(a)
        c = b.capitalize()
        return c
    return dic.get(word)

print(num_translate(dictionary, 'one'))
print(num_translate(dictionary, 'Two'))