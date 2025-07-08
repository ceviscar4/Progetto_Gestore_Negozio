import os
import pickle

from pathlib import Path


from moduli.Prodotto import Prodotto


class Gestore_magazzino:
    #file_magazzino="S:/Progetto Gestore Negozio/Dati/magazzino.pickle"


    def __init__(self):
        print("🛠️ Inizializzazione di Gestore_magazzino...")
        #self.cartella_dati=Path("Dati")
        #self.file_path = self.cartella_dati / "magazzino.pickle"
        #self.prodotti=self.carica_dati()
        self.file_path = Path("Dati/magazzino.pickle")
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self.prodotti = self.carica_dati() #Dizionario con codice:prodotto


    def carica_dati(self):
        try:
            if self.file_path.is_file():     #os.path.isfile(self.file_magazzino):
                print(f" file: {self.file_path} trovato")
                with open(self.file_path,"rb") as file:
                    self.prodotti=pickle.load(file)
                    if isinstance(self.prodotti,dict):
                        return self.prodotti
                    else:
                        print("⚠️ Il file non contiene un dizionario valido, creando uno nuovo.")
                        return {}


                #return pickle.load(file)

        except (FileNotFoundError,EOFError):
            return {}

    def salva_dati(self):
        try:
            #if os.path.isfile(self.file_path):
                with open(self.file_path,"wb") as file:
                    pickle.dump(self.prodotti,file,pickle.HIGHEST_PROTOCOL)
                print(f"i dati sono stati salvati in {self.file_path}, i prodotti sono: {self.prodotti}")

        except (IOError, pickle.PickleError) as e:
            print(f"Errore durante il salvataggio: {e}")



    #create: aggiungi un nuovo prodotto e salva nel file pickle
    def aggiungi_prodotto(self,codice,nome,prezzo,marca,quantita):
        if(codice in self.prodotti):
            print(f"⚠️ Errore: Il prodotto con il codice {codice} esiste già!")
            return
        nuovo_prodotto = Prodotto(codice,nome,prezzo,marca,quantita)
        self.prodotti[codice] = nuovo_prodotto
        self.salva_dati()
        print(f"✅ Prodotto {nome} codice {codice} aggiunto con successo!")

    #Update:modifica un prodotto esistente
    def modifica_prodotto(self,codice,nuovo_nome=None,nuovo_prezzo=None,nuova_quantita=None):
        if codice not in self.prodotti:
            print("⚠️ Errore: Prodotto non trovato!")
            return
        prodotto=self.prodotti[codice]
        if nuovo_nome:
            prodotto.nome=nuovo_nome
        if nuovo_prezzo:
            prodotto.prezzo=nuovo_prezzo
        if nuova_quantita is not None:
            prodotto.quantita=nuova_quantita
        self.salva_dati()
        print(f"✅ Prodotto {codice} aggiornato con successo!")

    #Delete:Rimuove un prodotto dal magazzino
    def rimuovi_prodotto(self,codice):
        self.prodotti = self.carica_dati()
        if codice in self.prodotti:
            del self.prodotti[codice]
            #nome=self.prodotti[codice].nome

            self.salva_dati()
            print(f"✅ Prodotto {codice} rimosso!")
        else:
            print("⚠️ Errore: Prodotto non trovato!")


    #Ricerca i prodotti per nome
    def ricerca_prodotto(self,nome):
        prodotti_ricercati=[p for p in self.prodotti.values() if nome.lower() in p.nome.lower()]
        if prodotti_ricercati:
            print("\n 🔍 Risultati della ricerca:")
            for prodotto in prodotti_ricercati:
                print(prodotto)
        else:
            print("❌ Nessun prodotto trovato.")

    #Visualizza lista prodotti opzionalmente per nome
    def visualizza_prodotti(self,ordinati= False):
        if not self.prodotti:
            print("Il magazzino è vuoto!")
            return

        if ordinati:
            print("ordinati")
            lista_prodotti=sorted(self.prodotti.values(),key=lambda p:p.nome)
            for prodotto in lista_prodotti:
                print(prodotto)


    def vendi_prodotto(self, codice_prodotto, quantita):
        if codice_prodotto in self.prodotti:
            prodotto = self.prodotti[codice_prodotto]
            if prodotto.quantita >= quantita:
                prodotto.quantita -= quantita
                self.salva_dati()
                print(f"✅ Venduti {quantita} pezzi di {prodotto.nome}. Nuova giacenza: {prodotto.quantita}")
                return True
            else:
                print("Quantità insufficiente in magazzino!")
                return False
        else:
            print("Prodotto non trovato!")
            return False








