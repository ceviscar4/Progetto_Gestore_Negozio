import unittest
import pickle
from pathlib import Path
from Gestione.Gestore_magazzino import Gestore_magazzino

class TestGestoreMagazzino(unittest.TestCase):

    def setUp(self):
        # Creiamo un file pickle temporaneo nella cartella DatiTest
        self.test_dir = Path("DatiTest")
        self.test_dir.mkdir(exist_ok=True)
        self.test_file = self.test_dir / "magazzino_test.pickle"

        # Override del path del file per test
        self.gestore = Gestore_magazzino()
        self.gestore.file_path = self.test_file
        self.gestore.prodotti = {}  # Resetta i prodotti

    def tearDown(self):
        # Pulisci dopo il test
        if self.test_file.exists():
            self.test_file.unlink()
        if self.test_dir.exists():
            self.test_dir.rmdir()

    def test_aggiungi_prodotto(self):
        codice = "P001"
        nome = "Mouse Logitech"
        prezzo = 25.99
        marca = "Logitech"
        quantita = 10

        self.gestore.aggiungi_prodotto(codice, nome, prezzo, marca, quantita)

        self.assertIn(codice, self.gestore.prodotti)
        prodotto = self.gestore.prodotti[codice]

        self.assertEqual(prodotto.nome, nome)
        self.assertEqual(prodotto.prezzo, prezzo)
        self.assertEqual(prodotto.marca, marca)
        self.assertEqual(prodotto.quantita, quantita)

        # Verifica che il file sia stato salvato
        self.assertTrue(self.test_file.exists())

        # Carica il file e verifica che il prodotto sia presente
        with open(self.test_file, "rb") as file:
            dati_salvati = pickle.load(file)
            self.assertIn(codice, dati_salvati)
            self.assertEqual(dati_salvati[codice].nome, nome)


if __name__ == '__main__':
    unittest.main()
