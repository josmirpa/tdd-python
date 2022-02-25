from app.rot13_cipher import rot13



class TestClass:
    def test_rot13(self):
        assert suma("Hola Mundo") == "Ubyn Zhaqb"
        assert suma("test") == "grfg"
