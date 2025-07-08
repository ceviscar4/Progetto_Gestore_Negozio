import os.path
import pickle
from moduli.Cliente import Cliente
from pathlib import Path


class Gestione_Clienti:
    #file_clienti = "S:/Progetto Gestore Negozio/Dati/clienti.pickle"


    def __init__(self):
        self.file_clienti = Path("Dati/clienti.pickle")
        self.file_clienti.parent.mkdir(parents=True, exist_ok=True)
        self.clienti = self.carica_dati()

    #carica i dati in un dizionario
    def carica_dati(self):
        try:
            if self.file_clienti.is_file():
                print(f"file: {self.file_clienti} trovato")
                with open(self.file_clienti, "rb") as file:
                    self.clienti = pickle.load(file)
                    if isinstance(self.clienti,dict):
                        return self.clienti
                    else:
                        print("⚠️ Il file non contiene un dizionario valido, creando uno nuovo.")
                        return {}

        except (FileNotFoundError, EOFError):
             return {}

    #salva i dati in un file pickle
    def salva_dati(self):
        try:

                with open(self.file_clienti, "wb") as file:
                    pickle.dump(self.clienti, file, pickle.HIGHEST_PROTOCOL)
                print(f"i dati sono stati salvati in {self.file_clienti}, i prodotti sono: {self.clienti}")

        except (IOError, pickle.PickleError) as e:
            print(f"Errore durante il salvataggio: {e}")


    #aggiunge un cliente in lista
    def aggiungi_cliente(self,codice,nome,indirizzo,telefono,email):
        if(codice in self.clienti):
            print(f"Errore il cliente {nome} esiste già")
            return
        nuovo_cliente = Cliente(codice, nome, indirizzo, telefono, email)
        self.clienti[codice] = nuovo_cliente #[nome] da aggiungere a self.clienti se non va
        self.salva_dati()
        print(f"Cliente {nome} aggiunto con successo!")


    #modifica di alcune caratteristiche del cliente come nome e telefono
    def modifica_cliente(self,codice,nome,nuovo_nome=None,nuovo_indirizzo=None,nuovo_telefono=None,nuovo_email=None):
        if codice not in self.clienti:
            print("⚠️ Errore il cliente non esiste!")
            return
        cliente=self.clienti[nome]
        if nuovo_nome:
            cliente.nome=nuovo_nome
        if nuovo_indirizzo:
            cliente.indirizzo=nuovo_indirizzo
        if nuovo_telefono:
            cliente.telefono=nuovo_telefono
        if nuovo_email:
            cliente.email=nuovo_email
        self.salva_dati()
        print(f"✅ cliente {nome} aggiornato con successo")


    #rimuove un cliente dalla lista
    def rimuovi_cliente(self,codice):
        self.clienti = self.carica_dati()
        if codice in self.clienti:
            del self.clienti[codice]
            self.salva_dati()
            print(f"✅ Cliente {codice} rimosso!")
        else:
            print("⚠️ Errore: Cliente non trovato!")

    #ricerca i clienti per nome
    def ricerca_cliente(self,nome):
        clienti_ricercati = [p for p in self.clienti.values() if nome.lower() in p.nome.lower()]
        if clienti_ricercati:
            print("\n 🔍 Risultati della ricerca:")
            for cliente in clienti_ricercati:
                print(cliente)
        else:
            print("❌ Nessun cliente trovato.")

    #visualizza una lista clienti opzionalmente per nome
    def visualizza_clienti(self,ordinati=False):
        if not self.clienti:
            print("Il magazzino è vuoto!")
            return

        if ordinati:
            lista_clienti=sorted(self.clienti.values(),key=lambda p:p.nome)
            for cliente in lista_clienti:
                print(cliente)




