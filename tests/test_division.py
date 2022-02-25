from app.operaciones import division



class TestClass:
    def test_division(self):
        assert division(10, 5) == 2.0
        assert division(50, 5) == 10.0
