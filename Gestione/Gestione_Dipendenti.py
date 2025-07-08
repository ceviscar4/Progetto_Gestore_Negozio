import os
import pickle
from moduli.Dipendenti import Dipendenti
from pathlib import Path

class Gestione_Dipendenti:
    #file_dipendenti = "S:/Progetto Gestore Negozio/Dati/Dipendenti.pickle"


    def __init__(self):
        #self.cartella_dati=Path("Dati")
        #self.file_path = self.cartella_dati / "dipendenti.pickle"
        self.file_dipendenti = Path("Dati/dipendenti.pickle")
        self.file_dipendenti.parent.mkdir(parents=True, exist_ok=True)
        self.dipendenti = self.carica_dati()



    def carica_dati(self):
        try:
            #if os.path.isfile(self.file_dipendenti):   #self.file_dipendenti.is_file():
                print(f"file {self.file_dipendenti} trovato")  #os.path.isfile(self.file_dipendenti):
                with open(self.file_dipendenti, "rb") as file:
                   self.dipendenti = pickle.load(file)
                return self.dipendenti

        except (FileNotFoundError, EOFError):
             return {}


    def salva_dati(self):
        try:
            with open(self.file_dipendenti, "wb") as file:
                pickle.dump(self.dipendenti, file, pickle.HIGHEST_PROTOCOL)

        except (IOError, pickle.PickleError) as e:
            print(f"Errore durante il salvataggio: {e}")


    def aggiungi_dipendenti(self,codice,nome,mansione,telefono,email):
        if codice in self.dipendenti:
            print(f"❌ Il dipendente {nome} esiste già")
            return
        nuovo_dipendente = Dipendenti(codice, nome, mansione, telefono, email)
        self.dipendenti[codice] = nuovo_dipendente
        self.salva_dati()
        print(f"✅ Dipendente {nome} aggiunto!")


    def modifica_dipendenti(self,codice,nome,nuovo_nome=None,nuova_mansione=None,nuovo_telefono=None,nuova_email=None):
        if codice not in self.dipendenti:
            print(f"Il dipendente {nome} non esiste!")
            return
        dipendente = self.dipendenti[codice]
        if nuovo_nome:
            dipendente.nome=nuovo_nome
        if nuova_mansione:
            dipendente.mansione=nuova_mansione
        if nuovo_telefono:
            dipendente.telefono=nuovo_telefono
        if nuova_email:
            dipendente.email=nuova_email

        self.salva_dati()
        print(f"✅ dipendente {nome} aggiornato con successo")


    def rimuovi_dipendenti(self,codice):
        if codice in self.dipendenti:
            nome = self.dipendenti[codice].nome
            del self.dipendenti[codice]
            self.salva_dati()
            print(f"✅ Dipendente {nome} con il codice: {codice} rimosso!")
        else:
            print("⚠️ Errore: Dipendente non trovato!")


    def ricerca_dipendenti(self,nome):
        dipendenti_cercati = [p for p in self.dipendenti.values() if nome.lower() in p.nome.lower()]
        if dipendenti_cercati:
            print("\n 🔍 I risultati della ricerca:")
            for dipendente in dipendenti_cercati:
                print(dipendente)
        else:
            print("Nessun dipendente trovato.")


    def visualizza_dipendenti(self,ordinati=False):
        if not self.dipendenti:
            print("Non ci sono dipendenti!")
            return
        if ordinati:
            lista_dipendenti=sorted(self.dipendenti.values(),key=lambda p:p.nome)
            for dipendente in lista_dipendenti:
                print(dipendente)

