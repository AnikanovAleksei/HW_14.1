import pytest

from src.main import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def sample_product():
    return Product("Test Product", "This is a description", 100.0, 10)


@pytest.fixture
def sample_smartphone():
    return Smartphone("Test Smartphone", "This is a smartphone", 500.0, 5, "High", "S23", "256GB", "Black")


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass("Test LawnGrass", "This is lawn grass", 50.0, 20, "USA", "2 weeks", "Green")


def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "This is a description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10
    assert sample_product.color == ""


def test_repr(sample_product):
    expected_repr = "Product(Test Product, This is a description, 100.0, 10)"
    assert repr(sample_product) == expected_repr


def test_str(sample_product):
    expected_str = "Test Product, 100.0 руб. Остаток: 10 шт.\n"
    assert str(sample_product) == expected_str


def test_price_setter(sample_product):
    sample_product.price = 200.0
    assert sample_product.price == 200.0
    sample_product.price = -50
    assert sample_product.price == 200.0  # Price should not change due to negative value


def test_add_products(sample_product):
    other_product = Product("Other Product", "Description", 150.0, 5)
    assert sample_product + other_product == (100.0 * 10 + 150.0 * 5)


def test_category_creation(sample_product):
    category = Category("Test Category", "This is a category", [sample_product])
    assert category.name == "Test Category"
    assert category.description == "This is a category"
    assert len(category.products.split("\n")) == 3  # One product + empty line at the end


def test_add_product_to_category(sample_product):
    category = Category("Test Category", "This is a category", [])
    category.add_product(sample_product)
    assert len(category.products.split("\n")) == 3  # One product + empty line at the end


def test_add_invalid_product_to_category():
    category = Category("Test Category", "This is a category", [])
    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_smartphone_initialization(sample_smartphone):
    assert sample_smartphone.name == "Test Smartphone"
    assert sample_smartphone.description == "This is a smartphone"
    assert sample_smartphone.price == 500.0
    assert sample_smartphone.quantity == 5
    assert sample_smartphone.efficiency == "High"
    assert sample_smartphone.model == "S23"
    assert sample_smartphone.memory == "256GB"
    assert sample_smartphone.color == "Black"


def test_lawn_grass_initialization(sample_lawn_grass):
    assert sample_lawn_grass.name == "Test LawnGrass"
    assert sample_lawn_grass.description == "This is lawn grass"
    assert sample_lawn_grass.price == 50.0
    assert sample_lawn_grass.quantity == 20
    assert sample_lawn_grass.country == "USA"
    assert sample_lawn_grass.germination_period == "2 weeks"
    assert sample_lawn_grass.color == "Green"


# Написание теста на проверку метода класса `new_product`
def test_new_product():
    data = {"name": "New Product", "description": "New Description", "price": 300.0, "quantity": 15, "color": "Red"}
    new_product = Product.new_product(data)
    assert new_product.name == "New Product"
    assert new_product.description == "New Description"
    assert new_product.price == 300.0
    assert new_product.quantity == 15
    assert new_product.color == "Red"
