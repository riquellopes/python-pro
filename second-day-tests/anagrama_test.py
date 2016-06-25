import unittest


def ana_grama(palavra):
    return True


class AnagramaTest(unittest.TestCase):

    def test_ovo_e_um_anagrama(self):
        assert ana_grama("ovo")

    def test_(self):
        pass


if __name__ == "__main__":
    unittest.main()
