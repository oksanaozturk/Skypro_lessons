# Принцип разделения интерфейсов (Interface Segregation)
# Описание: сделайте интерфейсы (родительские абстрактные классы) более конкретными, а не общими.
#
# Подход к реализации: при необходимости создайте дополнительные интерфейсы (классы).

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


class PaymentProcessorSMS(PaymentProcessor):

    @abstractmethod
    def pay(self, order):
        pass

    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessorSMS):

    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Верификация SMS кода {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
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


class PaypalPaymentProcessor(PaymentProcessorSMS):

    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code):
        print(f"Верификация SMS кода {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Не авторизован")
        print("Обработка paypal платежа")
        print(f"Использование адреса электронной почты: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Клавиатура", 1, 2500)
order.add_item("SSD", 1, 7500)
order.add_item("USB-кабель", 2, 250)

print(order.total_price())
processor = PaypalPaymentProcessor("hi@company.com")
processor.auth_sms(465839)
processor.pay(order)


