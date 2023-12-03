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

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Обработка дебетового типа платежа")
            print(f"Проверка кода безопасности: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Обработка кредитного типа платежа")
            print(f"Проверка кода безопасности: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Неизвестный способ оплаты: {payment_type}")