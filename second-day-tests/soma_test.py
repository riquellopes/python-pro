import unittest


def soma(numero_one, numero_two):
    return 0


class SomaTest(unittest.TestCase):

    def test_soma_zero(self):
        resultado = soma(0, 0)
        self.assertEquals(0, resultado)


if __name__ == "__main__":
    unittest.main()
