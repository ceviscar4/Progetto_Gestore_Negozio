from Gestione.Gestore_magazzino import Gestore_magazzino


class ControllerMagazzino:
    def __init__(self):
        self.gestore_magazzino = Gestore_magazzino()

    def aggiungi_prodotto(self,codice, nome, prezzo, marca,quantita):
         self.gestore_magazzino.aggiungi_prodotto(codice, nome, prezzo, marca, quantita)

    def modifica_prodotto(self,codice,nuovo_nome=None,nuovo_prezzo=None,nuova_quantita=None):
         self.gestore_magazzino.modifica_prodotto(codice,nuovo_nome,nuovo_prezzo,nuova_quantita)

    def rimuovi_prodotto(self,codice):
         self.gestore_magazzino.rimuovi_prodotto(codice)

    def ricerca_prodotto(self,nome):
         self.gestore_magazzino.ricerca_prodotto(nome)

    def visualizza_prodotti(self,ordinati= False):
         self.gestore_magazzino.visualizza_prodotti(ordinati)
