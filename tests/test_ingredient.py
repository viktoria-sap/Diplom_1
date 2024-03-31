import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize("name, price", [
        ("Lettuce", 0.50),
        ("Tomato", 0.75)
    ])
    def test_get_price(self, name, price):
        ingredient = Ingredient("Vegetable", name, price)
        assert ingredient.get_price() == price

    def test_get_name(self):
        ingredient = Ingredient("Vegetable", "Biocotlets", 0.50)
        assert ingredient.get_name() == "Biocotlets"

    def test_get_type(self):
        ingredient = Ingredient("Vegetable", "Biocotlets", 0.50)
        assert ingredient.get_type() == "Vegetable"

