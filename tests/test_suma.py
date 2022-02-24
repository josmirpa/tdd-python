from app.operaciones import suma
from app.rot13_cipher import rot13


class TestClass:
    def test_rot13(self):
        assert rot13("a") == "n"
        assert rot13("b") == "o"


class TestClass:
    def test_suma(self):
        assert suma(4, 5) == 9
        assert suma(-1, -2) == -3
        assert suma(-7, 5) == -2
        assert suma(-7, 9) == 2

        
