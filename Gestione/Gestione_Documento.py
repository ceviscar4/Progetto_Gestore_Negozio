# Importa le classi di gestione già fatte

import os
import pickle
from datetime import datetime
from pathlib import Path

from Gestione.Gestione_Clienti import Gestione_Clienti
from Gestione.Gestione_Dipendenti import Gestione_Dipendenti
from Gestione.Gestore_magazzino import Gestore_magazzino
from moduli.Documento import Documento


# Classe GestioneDocumenti
class GestioneDocumenti:
    def __init__(self):
        # File in cui verranno salvati i documenti
        self.file_documenti = Path("Dati/documenti.pickle")
        self.file_documenti.parent.mkdir(parents=True, exist_ok=True)
        self.documenti = self.carica_documenti()

        # Istanzio le classi di gestione già esistenti
        self.gestione_clienti = Gestione_Clienti()
        self.gestione_dipendenti = Gestione_Dipendenti()
        self.gestione_magazzino = Gestore_magazzino()

    def carica_documenti(self):
        try:
            #if self.file_documenti.is_file():
                with open(self.file_documenti, "rb") as f:
                    docs = pickle.load(f)
                    if isinstance(docs, dict):
                        return docs
                    else:
                        print("⚠️ Il file non contiene un dizionario valido, inizializzo documenti vuoti.")
                        return {}
        except (FileNotFoundError, EOFError, pickle.PickleError):
            return {}

    def salva_documenti(self):
        try:
            with open(self.file_documenti, "wb") as f:
                pickle.dump(self.documenti, f, pickle.HIGHEST_PROTOCOL)
            print(f"✅ Documenti salvati: {self.documenti}")
        except Exception as e:
            print(f"Errore nel salvataggio dei documenti: {e}")

    def genera_id_documento(self):
        # Se esistono già documenti, prendi l'id massimo e incrementa
        if self.documenti:
            last_id = max(int(doc_id) for doc_id in self.documenti.keys())
        else:
            last_id = 0
        new_id = last_id + 1
        return str(new_id).zfill(5)

    # Metodi per recuperare (o creare) cliente, dipendente e prodotto
    def recupera_cliente(self, nome_cliente):
        # Cerca nel dizionario dei clienti (gestione_clienti.clienti)
        for cliente in self.gestione_clienti.clienti.values():
            if cliente.nome.lower() == nome_cliente.lower():
                return cliente
        return None

    def crea_cliente(self, nome_cliente):
        # Genera un codice cliente automatico
        new_code = str(len(self.gestione_clienti.clienti) + 1).zfill(5)
        # Qui inseriamo dati minimi; in un'applicazione reale si potrebbero richiedere più dati
        self.gestione_clienti.aggiungi_cliente(new_code, nome_cliente, "", "", "")
        return self.gestione_clienti.clienti[new_code]

    def recupera_dipendente(self, nome_dipendente):
        for dip in self.gestione_dipendenti.dipendenti.values():
            if dip.nome.lower() == nome_dipendente.lower():
                return dip
        return None



    def recupera_prodotto(self, nome_prodotto):
        for prod in self.gestione_magazzino.prodotti.values():
            if prod.nome.lower() == nome_prodotto.lower():
                return prod
        return None

    # Metodo principale per creare un documento (fattura od ordine)
    def crea_documento(self, data_input, nome_dipendente, nome_cliente, nome_prodotto, quantita):
        try:
            data = datetime.strptime(data_input, "%d-%m-%Y")
        except ValueError as e:
            print(f"Errore nella conversione della data: {e}")
            return None


        # Recupera cliente; se non esiste, lo crea
        cliente = self.recupera_cliente(nome_cliente)
        if cliente is None:
            print(f"Cliente '{nome_cliente}' non trovato. Verrà creato un nuovo cliente.")
            cliente = self.crea_cliente(nome_cliente)

        # Recupera dipendente;
        dipendente = self.recupera_dipendente(nome_dipendente)
        if dipendente is None:
            print(f"Dipendente '{nome_dipendente}' non trovato.")
            return None


        # Recupera prodotto; se non esiste, non possiamo creare il documento
        prodotto = self.recupera_prodotto(nome_prodotto)
        if prodotto is None:
            print(f"Prodotto '{nome_prodotto}' non trovato. Impossibile creare il documento.")
            return None

        # Determina il tipo di documento:
        # Se la quantità richiesta supera quella disponibile, il documento sarà un "Ordine"
        if quantita > prodotto.quantita:
            tipo_documento = "Ordine"
        else:
            tipo_documento = "Fattura"
            # Aggiorna la quantità disponibile per il prodotto solo nel caso di una fattura
            #prodotto.quantita -= quantita # Sottrae la quantità dal prodotto
            venduto=self.gestione_magazzino.vendi_prodotto(prodotto.codice,quantita)
            if not venduto:
                print("Operazione annullata: quantità insufficiente.")
                return None
            print(f"✅ Quantità aggiornata per il prodotto '{prodotto.nome}'. Nuova disponibilità: {prodotto.quantita}")

            # Genera l'id del documento e crea l'oggetto Documento
        id_doc = self.genera_id_documento()
        documento = Documento(id_doc, data, dipendente, cliente, prodotto, quantita, tipo_documento)
        self.documenti[id_doc] = documento
        self.salva_documenti()
        return documento

        # Elimina un documento dato il suo id

    def elimina_documento(self, id_doc):
        if id_doc in self.documenti:
            del self.documenti[id_doc]
            self.salva_documenti()
            print(f"✅ Documento {id_doc} eliminato!")
            return True
        else:
            print("⚠️ Errore: Documento non trovato!")
            return False

        # Modifica un documento dato il suo id; i parametri facoltativi consentono di aggiornare i campi desiderati

    def modifica_documento(self, id_doc, data_input=None, nome_dipendente=None, nome_cliente=None, nome_prodotto=None,
                           quantita=None):
        if id_doc not in self.documenti:
            print("⚠️ Errore: Documento non trovato!")
            return None

        doc = self.documenti[id_doc]

        if data_input is not None:
            try:
                new_data = datetime.strptime(data_input, "%d-%m-%Y")
                doc.data = new_data
            except ValueError as e:
                print(f"Errore nella conversione della data: {e}")

        if nome_dipendente is not None:
            dipendente = self.recupera_dipendente(nome_dipendente)
            if dipendente is None:
                dipendente = self.crea_dipendente(nome_dipendente)
            doc.dipendente = dipendente

        if nome_cliente is not None:
            cliente = self.recupera_cliente(nome_cliente)
            if cliente is None:
                cliente = self.crea_cliente(nome_cliente)
            doc.cliente = cliente

        if nome_prodotto is not None:
            prodotto = self.recupera_prodotto(nome_prodotto)
            if prodotto is None:
                print("⚠️ Prodotto non trovato, impossibile aggiornare questo campo.")
            else:
                doc.prodotto = prodotto



        if quantita is not None:
            doc.quantita = quantita
        # Ricalcola il tipo di documento in base alla nuova quantità e alla quantità disponibile del prodotto
            if quantita > doc.prodotto.quantita:
                doc.tipo_documento = "Ordine"
            else:
                doc.tipo_documento = "Fattura"

        self.salva_documenti()
        print(f"✅ Documento {id_doc} modificato!")
        return doc

        # Visualizza documento: se id_doc è None restituisce tutti i documenti, altrimenti solo quello corrispondente

    def visualizza_documento(self, id_doc=None):
        if id_doc is None:
            return list(self.documenti.values())
        else:
            if id_doc in self.documenti:
                return [self.documenti[id_doc]]
            else:
                print("⚠️ Documento non trovato!")
                return []

        # Ricerca documento per nome cliente: restituisce i documenti per cui il nome del cliente contiene la stringa cercata (case-insensitive)

    def ricerca_documento(self, nome_cliente):
        risultati = []
        for doc in self.documenti.values():
            if nome_cliente.lower() in doc.cliente.nome.lower():
                risultati.append(doc)
        return risultati

    def ricerca_documento_pdf(self, nome_cliente, tipo_documento):
        risultati = []
        nome_cliente = nome_cliente.lower().strip()
        tipo_documento = tipo_documento.lower().strip()
        for doc in self.documenti.values():
            print(f"Confronto cliente: '{nome_cliente}' in '{doc.cliente.nome.lower().strip()}'")
            print(f"Confronto tipo: '{tipo_documento}' == '{doc.tipo_documento.lower().strip()}'")
            if nome_cliente in doc.cliente.nome.lower().strip() and doc.tipo_documento.lower().strip() == tipo_documento:
                risultati.append(doc)
        print(f"Documenti trovati: {len(risultati)}")
        return risultati