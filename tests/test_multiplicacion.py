from app.operaciones import multiplicacion



class TestClass:
    def test_multiplicacion(self):
        assert multiplicacion(5, 4) == 20
        assert multiplicacion(2, 1) == 2
        assert multiplicacion(7, 5) == 35
        assert multiplicacion(9, 7) == 63
