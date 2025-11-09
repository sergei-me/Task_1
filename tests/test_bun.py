import pytest
from src.bun import Bun

@pytest.mark.parametrize(
    "name, price",
    [
        ("Бшеничная булочка", 100.0),
        ("Булочка с кунжутом", 120.5),
        ("Ржаная булочка", 90.0),
    ]
)
def test_bun(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name
    assert bun.get_price() == price

def test_zero_price():
    bun = Bun('Просто булочка', 0)

    assert bun.get_price() == 0
