# Принцип открытости/закрытости (Open/Closed)
# Описание: программные сущности (классы, модули, функции и т. п.) должны быть открыты для расширения,
# но закрыты для изменения.
#
# Подход к реализации: используйте абстрактные классы. Они могут определить, какие подклассы требуются,
# и усилить принцип единой ответственности, разделив обязанности кода.

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
    def pay(self, order, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Обработка дебетового типа платежа")
        print(f"Проверка кода безопасности: {security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Обработка кредитного типа платежа")
        print(f"Проверка кода безопасности: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Клавиатура", 1, 2500)
order.add_item("SSD", 1, 7500)
order.add_item("USB-кабель", 2, 250)

print(order.total_price())
processor = DebitPaymentProcessor()
processor.pay(order, "0372846")
