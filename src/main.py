from abc import ABC, abstractmethod


class MixinLog:
    def __init__(self):
        self.quantity = None
        self.price = None
        self.description = None
        self.name = None

    def log(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class BaseProduct(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass


class Product(MixinLog, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int, color: str = ""):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        # Инициализация атрибутов
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        # Вызов init после инициализации всех атрибутов
        super().log()

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.quantity

    @classmethod
    def new_product(cls, product_data: dict):
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]
        color = product_data.get("color", "")
        return cls(name, description, price, quantity, color)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product}\n"
        return result

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            result = total_price / len(self.__products)
            return result
        except ZeroDivisionError:
            return 0


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        super().__init__(name=name, description=description, price=price, quantity=quantity, color=color)


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        super().__init__(name=name, description=description, price=price, quantity=quantity, color=color)


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
