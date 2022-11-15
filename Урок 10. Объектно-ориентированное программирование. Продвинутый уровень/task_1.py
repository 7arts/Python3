class Matrix:

    def __init__(self, elems):
        self.elems = elems

    def __add__(self, other):
        return Matrix([map(sum, zip(*t)) for t in zip(self.elems, other.elems)])

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.elems]))


m1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
mt1 = Matrix(m1)
mt2 = Matrix(m2)
print(mt1)
print(mt2)
print(mt2 + mt1)

