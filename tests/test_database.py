from src.database import Database
from src.bun import Bun
from src.ingredient import Ingredient

def test_available_buns():
    db = Database()
    buns = db.available_buns()

    assert isinstance(buns, list)
    assert len(buns) == 3

    assert all(isinstance(b, Bun) for b in buns)

    assert buns[0].get_name() == 'black bun'
    assert buns[0].get_price() == 100


def test_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()

    assert isinstance(ingredients, list)
    assert len(ingredients) == 6

    assert all(isinstance(i, Ingredient) for i in ingredients)

    assert ingredients[1].get_name() == 'sour cream'
    assert ingredients[1].get_price() == 200
