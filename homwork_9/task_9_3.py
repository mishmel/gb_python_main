class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        print(f'employee: {self.surname} {self.name}')

    def get_total_income(self):
        income = self._income_wage + self._income_bonus
        print(income)


sorcerer = Position('Petr', 'Petrov', 'sorcerer', {'wage': 31000, 'bonus': 337})
sorcerer.get_full_name()
sorcerer.get_total_income()
