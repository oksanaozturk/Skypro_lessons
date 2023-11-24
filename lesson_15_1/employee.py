class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10
    # Переопределяем метод базового класса

    def __init__(self, first, last, pay, prog_lang):
        # Вызываем метод базового класса
        super().__init__(first, last, pay)
        # Дополнительный код
        self.prog_lang = prog_lang


if __name__ == '__main__':
    # dev_1 = Developer('Ivan', 'Ivanov', 60000, 'Python')
    # dev_2 = Developer('Petr', 'Petrov', 70000, 'Java')
    dev_1 = Developer('Ivan', 'Ivanov', 60000, 'Python')
    dev_1.apply_raise()
    print(dev_1.pay)
    print(dev_1.fullname())
