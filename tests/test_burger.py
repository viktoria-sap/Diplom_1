from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import pytest


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Rye bun", 1.50)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient("Lettuce", "Biocotlets", 0.50)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("Lettuce", "Biocotlets", 0.50)
        ingredient2 = Ingredient("Tomato", "Biocotlets", 0.75)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("Lettuce", "Biocotlets", 0.50)
        ingredient2 = Ingredient("Tomato", "Biocotlets", 0.75)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    def test_get_price(self):
        burger = Burger()
        bun = Bun("Rye bun", 1.50)
        ingredient1 = Ingredient("Lettuce", "Biocotlets", 0.50)
        ingredient2 = Ingredient("Tomato", "Biocotlets", 0.75)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 4.25

    def test_get_receipt(self):
        bun = Bun("Rye bun", 1.50)
        ingredient1 = Ingredient("Lettuce", "Biocotlets", 0.50)

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)

        expected_receipt = (f'(==== {bun.get_name()} ====)\n'
                            f'= {str(ingredient1.get_type()).lower()} {ingredient1.get_name()} =\n'
                            f'(==== {bun.get_name()} ====)\n'
                            f'\nPrice: {burger.get_price()}')

        assert expected_receipt == burger.get_receipt()
