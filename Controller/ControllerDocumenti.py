


# ControllerDocumenti.py
from Gestione.Gestione_Documento import GestioneDocumenti

class ControllerDocumenti:
    def __init__(self):
        self.gestione_documenti = GestioneDocumenti()

    def aggiungi_documento(self, data_input, nome_dipendente, nome_cliente, nome_prodotto, quantita):
        """
        Crea e aggiunge un documento.
        data_input: stringa nel formato "dd/mm/yyyy"
        nome_dipendente, nome_cliente, nome_prodotto: stringhe
        quantita: intero
        """
        return self.gestione_documenti.crea_documento(
            data_input, nome_dipendente, nome_cliente, nome_prodotto, quantita
        )

    def modifica_documento(self, id_doc, data_input=None, nome_dipendente=None, nome_cliente=None, nome_prodotto=None, quantita=None):
        """
        Modifica il documento con id_doc aggiornando i campi passati come parametro.
        I parametri facoltativi (default None) non vengono modificati se non forniti.
        """
        return self.gestione_documenti.modifica_documento(
            id_doc, data_input, nome_dipendente, nome_cliente, nome_prodotto, quantita
        )

    def rimuovi_documento(self, id_doc):
        """
        Rimuove il documento identificato da id_doc.
        """
        return self.gestione_documenti.elimina_documento(id_doc)

    def visualizza_documento(self, id_doc=None):
        """
        Se id_doc è None restituisce tutti i documenti,
        altrimenti restituisce una lista contenente solo il documento corrispondente.
        """
        return self.gestione_documenti.visualizza_documento(id_doc)

    def ricerca_documento(self, nome_cliente):
        """
        Restituisce una lista di documenti in cui il nome del cliente contiene la stringa cercata (case-insensitive).
        """
        return self.gestione_documenti.ricerca_documento(nome_cliente)

    def ricerca_documento_pdf(self,nome_cliente, tipo_documento):
        return self.gestione_documenti.ricerca_documento_pdf(nome_cliente, tipo_documento)



