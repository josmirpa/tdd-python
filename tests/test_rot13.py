from app.operaciones import rot13


class TestClass:
    def test_suma(self):
        assert rot13("a") == "n"
        assert rot13("b") == "o"
