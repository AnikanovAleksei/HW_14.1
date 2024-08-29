import pytest

from src.main import Category, Product


def test_product_initialization():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_setter():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product.price = 200000.0
    assert product.price == 200000.0
    product.price = -100.0
    assert product.price == 200000.0  # Цена не должна измениться на отрицательную


def test_product_str():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_product_addition():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product1 + product2 == 180000.0 * 5 + 210000.0 * 8


def test_category_initialization():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                        [product1, product2])
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                        [product1])
    category.add_product(product2)
    assert Category.product_count == 4


def test_category_str():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                        [product1, product2])
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


if __name__ == '__main__':
    pytest.main()
