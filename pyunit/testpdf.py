import unittest
import os
from datetime import datetime
from Gestione.GeneraPDF import GestorePDF

# Mock minimo
class Documento:
    class Cliente:
        nome = "Mario Rossi"
        codice = "C001"
        indirizzo = "Via Roma 10"
        telefono = "123456789"
        email = "mario@example.com"
    class Dipendente:
        nome = "Luca Verdi"
    class Prodotto:
        codice = "P001"
        nome = "Mouse"
        marca = "Logitech"
        prezzo = 20.0

    cliente = Cliente()
    dipendente = Dipendente()
    prodotto = Prodotto()
    tipo_documento = "fattura"
    id_documento = "F123"
    data = datetime(2025, 5, 21)
    quantita = 2

class TestPDF(unittest.TestCase):
    def test_genera_pdf(self):
        gestore = GestorePDF("Dati/TestPDF")
        doc = Documento()
        gestore.genera_pdf(doc)

        nome_atteso = "Mario_Rossi_fattura_F123.pdf"
        percorso_atteso = os.path.join("Dati/TestPDF", nome_atteso)
        self.assertTrue(os.path.exists(percorso_atteso))

        # Pulizia
        os.remove(percorso_atteso)
        os.rmdir("Dati/TestPDF")

if __name__ == '__main__':
    unittest.main()