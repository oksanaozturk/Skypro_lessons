# Принцип подстановки Барбары Лисков (Liskov Substitution)
# Описание: если класс Parent является родительским классу Child,
# то любые методы класса Parent могут заменяться методами класса Child без возникновения ошибок в программе.

# Подход к реализации: используйте аргументы конструктора, чтобы обеспечить гибкость наследования.

from abc import ABC, abstractmethod


# Класс Order не менялся.
class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        return sum(quantities * prices for quantities, prices in zip(self.quantities, self.prices))


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Обработка дебетового типа платежа")
        print(f"Проверка кода безопасности: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Обработка кредитного типа платежа")
        print(f"Проверка кода безопасности: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print("Обработка paypal платежа")
        print(f"Использование адреса электронной почты: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Клавиатура", 1, 2500)
order.add_item("SSD", 1, 7500)
order.add_item("USB-кабель", 2, 250)

print(order.total_price())
processor = PaypalPaymentProcessor("hi@company.com")
processor.pay(order)