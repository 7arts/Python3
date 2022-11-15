class Date:

    def __init__(self, date: str):
        self.__date = date

    @staticmethod
    def is_valid(date: str):
        day: int
        month: int
        year: int
        try:
            day, month, year = Date.split_to_numb(date)
        except:
            return f'False: неправильно записанна дата'

        if not 1 <= month <= 12:
            return f'False: неправильный месяц'

        if not 0 <= year:
            return f'False: неправильный год'

        if not 1 <= day <= 31:
            return f'False: неправильный день'

        if month in [4, 6, 9, 11] and day == 31:  #когда в месяце не 31 день
            return f'False: в этом месяце 30 дней'

        if (                                                  #месяц февраль
            month == 2 and
            day == 29 and
            year % 4 == 0 and
            year % 100 == 0 and
            year % 400 == 0
        ):
            return f'високосный год'
        if month == 2 and day >= 28:
            return f'False: в этом месяце 28 дней'
        return True

    @classmethod
    def split_to_numb(self, date: str):
        try:
            return(list(map(int, date.split("-"))))
        except:
            raise ValueError


print(Date.is_valid('18-04-2022'))
print(Date.is_valid('18.04.2022'))
print(Date.is_valid('18-13-2022'))
print(Date.is_valid('0-04-2022'))
print(Date.is_valid('31-04-2022'))
print(Date.is_valid('29-02-2000'))
print(Date.is_valid('29-02-2001'))
