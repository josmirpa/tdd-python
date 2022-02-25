from app.operaciones import cociente

class TestClass:
    def test_cociente(self):
        assert cociente(11, 5) == 2
