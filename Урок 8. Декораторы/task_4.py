from functools import wraps


def val_checker(callback):
    def checker(func):
        @wraps(func)
        def wrapper(x):
            if callback(x):
                return func(x)

            raise ValueError

        return wrapper

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)
