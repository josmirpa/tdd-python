from app.operaciones import rot13


class TestClass:
    def test_suma(self):
        assert rot13("A") == "N"
        assert rot13("B") == "O"
