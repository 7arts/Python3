class AllNumb(Exception):

    def __init__(self, *args):
        self._args = args

lst = []
while True:
    try:
        inp = input("введите число: ")
        if inp == "stop":
            break
        elif not inp.isdigit():
            raise AllNumb()
        else:
            lst.append(int(inp))
    except AllNumb:
        print("Вы ввели не число ")

print('Весь список чисел: ', lst)
