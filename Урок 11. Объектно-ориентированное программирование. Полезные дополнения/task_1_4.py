class MyComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        sum_a = self.a + other.a
        sum_b = self.b + other.b
        return MyComplex(sum_a, sum_b)

    def __mul__(self, other):
        pr_a = self.a * other.a - self.b * other.b
        pr_b = self.b * other.a + self.a * other.b
        return MyComplex(pr_a, pr_b)


z1 = MyComplex(1, 2)
z2 = MyComplex(2, 3)

print(f"({z1}) + ({z2}) = ", z1 + z2)
print(f"({z1}) * ({z2}) = ", z1 * z2)
