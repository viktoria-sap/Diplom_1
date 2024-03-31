import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", [("Rye bun", 1.50), ("Burger Bun", 2.00)])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [("Rye bun", 1.50), ("Burger Bun", 2.00)])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

