class Zero(Exception):
    def __init__(self, *args):
        self._args = args

a = 0
b = 0
try:
    a = float(input("введите число а: "))
    b = float(input("введите число b: "))
except:
    print("некорректное число")
    exit(1)

try:
    if b == 0:
        raise Zero
    print(f"{a}/{b} = {a / b}")
except Zero:
    print("Деление на ноль")
    
