class Cell:

    def __init__(self, cells):
        self.__cells = cells

    def __add__(self, other):
        return Cell(self._get_size() + other._get_size())

    def __sub__(self, other):
        if self._get_size() < other._get_size():
            raise ValueError
        return Cell(self._get_size() - other._get_size())

    def __mul__(self, other):
        return Cell(self._get_size() * other._get_size())

    def __floordiv__(self, other):
        return Cell(self._get_size() // other._get_size())

    def _get_cells(self):
        return str(self).replace("Cell(", "").replace(")", "")

    def _get_size(self):
        return self._get_cells().count("*")

    def __str__(self) -> str:
        return f"Cell({'*'*self.__cells})"

    def make_order(self, split_cell):
        if split_cell == 0:
            raise ValueError
        if split_cell >= self._get_size():
            return self._get_cells()
        size = self._get_size()
        return "".join([f"{x}\n" if i % split_cell == 0 and i != size else x
                        for i, x in enumerate(self._get_cells(), start=1)])


Cell_1 = Cell(3)
Cell_2 = Cell(2)
Cell_3 = Cell(13)

print(Cell_3 // Cell_2)
print(Cell_2 * Cell_1)
print(Cell_2 + Cell_1)
print(Cell_3 - Cell_1)
print(Cell.make_order(Cell_3, 5))
