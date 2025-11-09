import pytest
from src.ingredient import Ingredient
from src.ingredient_types import IngredientType

@pytest.mark.parametrize(
    "ingredient_type, name, price",
    [
        (IngredientType.SAUCE, 'кетчуп', 30.0),
        (IngredientType.SAUCE, 'майонез', 40.0),
        (IngredientType.FILLING, 'бекон', 60.0),
        (IngredientType.FILLING, 'халапенью', 70.0)
    ]
)
def test_ingredients(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
    assert isinstance(ingredient.get_price(), float)
