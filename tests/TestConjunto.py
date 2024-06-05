import unittest
from KataTDD.src.logica.Conjunto import Conjunto
class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5])
        self.assertEqual(5, conjunto.promedio())

    def test_conjunto_dosElementos_retornaPromedioElementos(self):
        conjunto = Conjunto([5, 7])
        self.assertEqual(6, conjunto.promedio())

    def test_conjunto_nElementos_retornaPromedioNElementos(self):
        conjunto = Conjunto([2, 4, 8, 9, 10, 15])
        self.assertEqual((2 + 4 + 8 + 9 + 10 + 15) / 6, conjunto.promedio())

    def test_promedio_ponderado(self):
        conjunto = Conjunto([2, 3, 4])
        pesos = [1, 2, 3]
        self.assertAlmostEqual(3.3333333333333335, conjunto.promedio_ponderado(pesos), places=10)

if __name__ == '__main__':
    unittest.main()
