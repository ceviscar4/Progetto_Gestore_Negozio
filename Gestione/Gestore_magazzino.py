

class Gestore_magazzino:
    def __init__(self):
        self.prodotti = {} #Dizionario con codice:prodotto

    #create: aggiungi un nuovo prodotto
    def aggiungi_prodotto(self,codice,nome,prezzo,marca,quantità):
        if(codice in self.prodotti):
            print(f"⚠️ Errore: Il prodotto con il codice {codice} esiste già!")
            return
        nuovo_prodotto = prodotto(codice,nome,prezzo,marca,quantità)
        self.prodotti[codice] = nuovo_prodotto
        print(f"✅ Prodotto {nome} aggiunto con successo!")

    #Update:modifica un prodotto esistente
    def modifica_prodotto(self,codice,nuovo_nome=None,nuovo_prezzo=None,nuova_quantità=None):
        if codice not in self.prodotti:
            print("⚠️ Errore: Prodotto non trovato!")
            return
        prodotto=self.prodotti[codice]
        if nuovo_nome:
            prodotto.nome=nuovo_nome
        if nuovo_prezzo:
            prodotto.prezzo=nuovo_prezzo
        if nuova_quantità is not None:
            prodotto.quantità=nuova_quantità
        print(f"✅ Prodotto {codice} aggiornato con successo!")

    #Delete:Rimuove un prodotto dal magazzino
    def rimuovi_prodotto(self,codice):
        if codice in self.prodotti:
            nome=self.prodotti[codice].nome
            del self.prodotti[codice]
            print(f"✅ Prodotto {nome} rimosso!")
        else:
            print("⚠️ Errore: Prodotto non trovato!")



