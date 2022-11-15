import time
import sys

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def my_set(*argv):
    answ = set()
    for elem in argv:
        if not elem in answ:
            answ.add(elem)
        else:
            answ.remove(elem)
    return [x for x in argv if x in answ]


t = time.perf_counter()
result = my_set(*src)
print(result)
print("sp: ", sys.getsizeof(result))
print("time: ", time.perf_counter() - t)