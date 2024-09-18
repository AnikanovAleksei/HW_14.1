import pytest
from src.main import Product, Category, Smartphone, LawnGrass  # Замените your_module на имя вашего модуля


def test_product_initialization():
    product = Product("Test Product", "Description", 100.0, 10)
    assert product.get_name() == "Test Product"
    assert product.get_description() == "Description"
    assert product.get_price() == 100.0
    assert product.get_quantity() == 10


def test_product_initialization_with_zero_quantity():
    with pytest.raises(ValueError):
        Product("Test Product", "Description", 100.0, 0)


def test_product_addition():
    product1 = Product("Product 1", "Description 1", 100.0, 2)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    total_price = product1 + product2
    assert total_price == 800.0


def test_category_initialization():
    product1 = Product("Product 1", "Description 1", 100.0, 2)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    category = Category("Test Category", "Description", [product1, product2])
    assert category.name == "Test Category"
    assert category.description == "Description"
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product():
    product1 = Product("Product 1", "Description 1", 100.0, 2)
    category = Category("Test Category", "Description", [product1])
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    category.add_product(product2)
    assert Category.product_count == 4


def test_category_middle_price():
    product1 = Product("Product 1", "Description 1", 100.0, 2)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    category = Category("Test Category", "Description", [product1, product2])
    assert category.middle_price() == 150.0


def test_category_middle_price_empty():
    category = Category("Empty Category", "Description", [])
    assert category.middle_price() == 0


def test_smartphone_initialization():
    smartphone = Smartphone("Smartphone", "Description", 500.0, 5, "High", "Model X", "128GB", "Black")
    assert smartphone.get_name() == "Smartphone"
    assert smartphone.get_description() == "Description"
    assert smartphone.get_price() == 500.0
    assert smartphone.get_quantity() == 5
    assert smartphone.efficiency == "High"
    assert smartphone.model == "Model X"
    assert smartphone.memory == "128GB"
    assert smartphone.color == "Black"


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass("Lawn Grass", "Description", 10.0, 100, "USA", "10 days", "Green")
    assert lawn_grass.get_name() == "Lawn Grass"
    assert lawn_grass.get_description() == "Description"
    assert lawn_grass.get_price() == 10.0
    assert lawn_grass.get_quantity() == 100
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "10 days"
    assert lawn_grass.color == "Green"