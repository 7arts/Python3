def type_logger(func):
        def decor(*argv):
            calc = func(*argv)
            if len(argv) == 1:
                print('calc_cube(' + f"{argv[0]}:{type(argv[0])}" + ")")
            else:
                for i in argv:
                    print('calc_cube(' + f"{i}:{type(i)}" + ")")
            return calc
        return decor


@ type_logger
def calc_cube(x, *argv):
    """ cube of args """
    return x ** 3


a = calc_cube(5, 7, 1335)
print(a)
