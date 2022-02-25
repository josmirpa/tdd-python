from app.operaciones import resto

class TestClass:
    def test_resto(self):
        assert resto(11, 5) == 1
