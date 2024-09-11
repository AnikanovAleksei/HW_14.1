import pytest

from src.main import Category, Product, Smartphone, LawnGrass


def test_product_initialization():
    product = Product(name="Test Product", description="A test product", price=100.0, quantity=10)
    assert product.get_name() == "Test Product"
    assert product.get_description() == "A test product"
    assert product.get_price() == 100.0
    assert product.get_quantity() == 10


def test_product_price_setter():
    product = Product(name="Test Product", description="A test product", price=100.0, quantity=10)
    product.price = 200.0
    assert product.get_price() == 200.0


def test_product_addition():
    product1 = Product(name="Product 1", description="Description 1", price=100.0, quantity=10)
    product2 = Product(name="Product 2", description="Description 2", price=200.0, quantity=5)
    total_price = product1 + product2
    assert total_price == 2000.0


def test_category_initialization():
    products = [
        Product(name="Product 1", description="Description 1", price=100.0, quantity=10),
        Product(name="Product 2", description="Description 2", price=200.0, quantity=5)
    ]
    category = Category(name="Test Category", description="A test category", products=products)
    assert category.name == "Test Category"
    assert category.description == "A test category"
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product():
    products = [
        Product(name="Product 1", description="Description 1", price=100.0, quantity=10),
        Product(name="Product 2", description="Description 2", price=200.0, quantity=5)
    ]
    category = Category(name="Test Category", description="A test category", products=products)
    new_product = Product(name="Product 3", description="Description 3", price=300.0, quantity=3)
    category.add_product(new_product)
    assert Category.product_count == 5


def test_smartphone_initialization():
    smartphone = Smartphone(name="Smartphone 1", description="A smartphone", price=500.0, quantity=5, efficiency="High",
                            model="Model X", memory="128GB", color="Black")
    assert smartphone.get_name() == "Smartphone 1"
    assert smartphone.get_description() == "A smartphone"
    assert smartphone.get_price() == 500.0
    assert smartphone.get_quantity() == 5
    assert smartphone.efficiency == "High"
    assert smartphone.model == "Model X"
    assert smartphone.memory == "128GB"
    assert smartphone.color == "Black"


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass(name="Lawn Grass 1", description="A lawn grass", price=10.0, quantity=100, country="USA",
                           germination_period="2 weeks", color="Green")
    assert lawn_grass.get_name() == "Lawn Grass 1"
    assert lawn_grass.get_description() == "A lawn grass"
    assert lawn_grass.get_price() == 10.0
    assert lawn_grass.get_quantity() == 100
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "2 weeks"
    assert lawn_grass.color == "Green"
