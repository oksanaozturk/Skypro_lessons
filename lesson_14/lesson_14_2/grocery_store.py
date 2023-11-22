class Product:
    def __init__(self, name: str, price: int, count: int) -> None:
        """Инициализация класса Продукт"""
        self.name = name
        self.price = price
        self.__count = count

    @property
    def count(self):
        return self.__count

    def sale(self, sale_count):
        """Метод реалицующий продажу товара"""
        self.__count -= sale_count

    def fill(self, fill_count):
        """Метод реалицующий поступление товаров на склад"""
        self.__count += fill_count


class Category:

    def __init__(self, name: str, products: list[str]) -> None:
        self.name = name
        self.__products = products
        self.__is_active = True

    @property
    def products(self):
        return self.__products

    @property
    def is_active(self):
        return self.__is_active

    def remove(self, product_index):
        del self.__products[product_index]

    def __add__(self, product_item):
        self.__products.append(product_item)


class Store:

    def __init__(self, categories):
        self.__categories = categories
        tmp = []
        for cat in categories:
            if cat.is_active:
                tmp.append(cat)
        return


if __name__ == "__main__":
    product = Product('Стул', 1500, 10)

    # TestCase#1 for class Product __init__
    assert product.name == 'Стул'
    assert product.price == 1500
    assert product.count == 10

    # TestCase#2 Продажа товара
    product.sale(1)
    assert product.count == 9

    # TestCase#3 Пополнение склада
    product.fill(1)
    assert product.count == 10

    category = Category('Стулья', [product])

    # TestCase#4 for class Category __init__
    assert category.name == 'Стулья'
    assert category.products == [product]

    # TestCase#5 Удаление товара
    category.remove(0)
    assert category.products == []

    # TestCase#6 Добавление товара
    category + product
    assert category.products == [product]
