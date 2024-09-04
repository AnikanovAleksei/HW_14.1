import pytest

from src.main import Category, Product, Smartphone, LawnGrass


def test_product_creation():
    product_data = {
        "name": "Test Product",
        "description": "This is a test product",
        "price": 100.0,
        "quantity": 10,
        "color": "Red"
    }
    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 100.0
    assert product.quantity == 10
    assert product.color == "Red"


def test_product_price_setter():
    product = Product("Test Product", "This is a test product", 100.0, 10, "Red")
    product.price = 200.0
    assert product.price == 200.0
    product.price = -50.0
    assert product.price == 200.0


def test_product_addition():
    product1 = Product("Product 1", "Description 1", 100.0, 5, "Blue")
    product2 = Product("Product 2", "Description 2", 200.0, 3, "Green")
    total_price = product1 + product2
    assert total_price == 1100.0


def test_category_creation():
    product1 = Product("Product 1", "Description 1", 100.0, 5, "Blue")
    product2 = Product("Product 2", "Description 2", 200.0, 3, "Green")
    category = Category("Test Category", "This is a test category", [product1, product2])
    assert category.name == "Test Category"
    assert category.description == "This is a test category"
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product():
    product1 = Product("Product 1", "Description 1", 100.0, 5, "Blue")
    product2 = Product("Product 2", "Description 2", 200.0, 3, "Green")
    category = Category("Test Category", "This is a test category", [product1])
    category.add_product(product2)
    assert Category.product_count == 4
    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_smartphone_creation():
    smartphone = Smartphone("Test Smartphone", "This is a test smartphone", 500.0, 10, 95.0, "Model X", 256, "Black")
    assert smartphone.name == "Test Smartphone"
    assert smartphone.description == "This is a test smartphone"
    assert smartphone.price == 500.0
    assert smartphone.quantity == 10
    assert smartphone.efficiency == 95.0
    assert smartphone.model == "Model X"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"


def test_lawn_grass_creation():
    lawn_grass = LawnGrass("Test Grass", "This is a test grass", 50.0, 20, "USA", "7 days", "Green")
    assert lawn_grass.name == "Test Grass"
    assert lawn_grass.description == "This is a test grass"
    assert lawn_grass.price == 50.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "7 days"
    assert lawn_grass.color == "Green"
