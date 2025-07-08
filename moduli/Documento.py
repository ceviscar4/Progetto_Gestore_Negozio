

class Documento:
    def __init__(self, id_documento, data, dipendente, cliente, prodotto, quantita, tipo_documento):
        self.id_documento = id_documento
        self.data = data
        self.dipendente = dipendente
        self.cliente = cliente
        self.prodotto = prodotto
        self.quantita = quantita
        self.tipo_documento = tipo_documento

    def __str__(self):
        data_str = self.data.strftime("%d/%m/%Y")
        return (f"Documento {self.id_documento} - {self.tipo_documento} del {data_str}\n"
                f"Dipendente: {self.dipendente.nome}\n"
                f"Cliente: {self.cliente.nome}\n"
                f"Indirizzo Cliente: {self.cliente.indirizzo}\n"
                f"Telefono: {self.cliente.telefono}\n"
                f"Email: {self.cliente.email}\n"
                f"Codice prodotto: {self.prodotto.codice}"
                f"Prodotto: {self.prodotto.nome} x {self.quantita}"
                f"Marca: {self.prodotto.marca}\n"
                f"Prezzo: {self.prodotto.prezzo}\n"




                )