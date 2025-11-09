"""
Перечисление с типами ингредиентов.
SAUCE – соус
FILLING – начинка
"""
from enum import Enum

class IngredientType(Enum):
    SAUCE = "SAUCE"
    FILLING = "FILLING"
