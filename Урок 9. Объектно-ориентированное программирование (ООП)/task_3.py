class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


res = Position("Artem", "Medvedev", "Programmer", 60000, 20000)
print(res.get_full_name())
print(res.position)
print(res.get_total_income())
