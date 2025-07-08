import unittest
from moduli.Prodotto import Prodotto

class ProdottoTest(unittest.TestCase):
    def setUp(self):
        self.p = Prodotto("P001", "Mouse Logitech", 25.99, "Logitech", 10)

    def test_getters(self):
        self.assertEqual(self.p.nome, "Mouse Logitech")
        self.assertEqual(self.p.quantita, 10)
        self.assertEqual(self.p.codice, "P001")
        self.assertEqual(self.p.prezzo, 25.99)
        self.assertEqual(self.p.marca, "Logitech")

    def test_setters(self):
        p = Prodotto("P002", "Tastiera", 30.0, "HP", 3)
        p.set_nome("Tastiera Meccanica")
        p.set_prezzo(45.0)
        p.set_quantita(10)
        p.set_marca("Corsair")
        self.assertEqual(p.get_nome(), "Tastiera Meccanica")
        self.assertEqual(p.get_prezzo(), 45.0)
        self.assertEqual(p.get_quantita(), 10)
        self.assertEqual(p.get_marca(), "Corsair")

if __name__ == '__main__':
        unittest.main()
