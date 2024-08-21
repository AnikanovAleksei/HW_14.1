import pytest

from src.main import Category, Product  # Замените your_module на имя вашего модуля


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def product4():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def category1(product1, product2, product3):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации," "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def category2(product4):
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром," "станет вашим другом и помощником",
        [product4],
    )


def test_product_initialization(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_category_initialization(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации," "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_product_count(category1, category2):
    assert Category.product_count == 4


def test_category_count(category1, category2):
    assert Category.category_count == 2


def test_category_products(category1, product1, product2, product3):
    assert product1 in category1.products
    assert product2 in category1.products
    assert product3 in category1.products


def test_category_products_length(category1, category2):
    assert len(category1.products) == 3
    assert len(category2.products) == 1
