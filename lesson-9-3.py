class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Full name is {self.name} {self.surname}')

    def get_total_income(self):
        print(f'total income is {sum(self._income.values())}')


worker_1 = Position('Her', 'He', 'Accountant', 100000, 10000)
worker_1.get_total_income()
worker_1.get_full_name()
