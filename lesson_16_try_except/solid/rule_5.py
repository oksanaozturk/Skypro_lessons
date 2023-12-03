# Принцип инверсии зависимостей (Dependency Inversion)
# Описание: сделать классы зависимыми от абстрактных классов, а не от обычных классов.
#
# Подход к реализации: наследовать классы от абстрактных классов.

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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class AuthorizerSMS(Authorizer):

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Верификация SMS кода {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class AuthorizerRobot(Authorizer):

    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Не авторизован")
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

    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Не авторизован")
        print("Обработка paypal платежа")
        print(f"Использование адреса электронной почты: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Клавиатура", 1, 2500)
order.add_item("SSD", 1, 7500)
order.add_item("USB-кабель", 2, 250)

print(order.total_price())
authorizer = AuthorizerRobot()
# authorizer.verify_code(465839)
authorizer.not_a_robot()
processor = PaypalPaymentProcessor("hi@company.com", authorizer)
processor.pay(order)