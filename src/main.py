from abc import ABC, abstractmethod


class MixinLog:
    def init(self, *args, **kwargs) -> None:
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
        # Инициализация атрибутов
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        # Вызов init после инициализации всех атрибутов
        super().init()

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
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)