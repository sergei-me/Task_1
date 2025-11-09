import pytest
from unittest.mock import MagicMock
from src.burger import Burger

@pytest.fixture
def bun_mock():
    bun = MagicMock()
    bun.get_name.return_value = 'Булочка'
    bun.get_price.return_value = 80
    return bun

@pytest.fixture
def ingredient_mock():
    ingredient = MagicMock()
    ingredient.get_type.return_value = 'FILLING'
    ingredient.get_name.return_value = 'сыр'
    ingredient.get_price.return_value = 90
    return ingredient

def test_set_buns(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    assert burger.bun == bun_mock

def test_add_ingredient(ingredient_mock):
    burger = Burger()
    burger.add_ingredient(ingredient_mock)
    assert ingredient_mock in burger.ingredients

def test_remove_ingredient(ingredient_mock):
    burger = Burger()
    burger.add_ingredient(ingredient_mock)
    burger.add_ingredient(ingredient_mock)

    burger.remove_ingredient(0)

    assert len(burger.ingredients) == 1

def test_move_ingredient(ingredient_mock):
    burger = Burger()

    ing1 = MagicMock()
    ing1.get_name.return_value = "инг_1"

    ing2 = MagicMock()
    ing2.get_name.return_value = "инг_2"

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    burger.move_ingredient(0, 1)

    assert burger.ingredients[0] == ing2
    assert burger.ingredients[1] == ing1

def test_get_price(bun_mock, ingredient_mock):
    burger = Burger()
    burger.set_buns(bun_mock)

    ing1 = MagicMock()
    ing1.get_price.return_value = 30.0

    ing2 = MagicMock()
    ing2.get_price.return_value = 60.0

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    expected_price = 80 * 2 + 30.0 + 60.0

    assert burger.get_price() == expected_price

def test_get_receipt(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)

    ing1 = MagicMock()
    ing1.get_type.return_value = "FILLING"
    ing1.get_name.return_value = "сыр"
    ing1.get_price.return_value = 60.0

    ing2 = MagicMock()
    ing2.get_type.return_value = "SAUCE"
    ing2.get_name.return_value = "кетчуп"
    ing2.get_price.return_value = 30.0

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    receipt = burger.get_receipt()

    assert "(==== Булочка ====)" in receipt
    assert "= filling сыр =" in receipt
    assert "= sauce кетчуп =" in receipt
    assert "Price: 250.0" in receipt

