from moduli.Posizione import Posizione


class Prodotto:
    def __init__(self, codice, nome, prezzo, marca, quantita):
        self.nome = nome
        self.prezzo = float(prezzo)
        self.quantita = int(quantita)
        self.marca = marca
        self.codice = codice
        self.posizione = None

    def get_nome(self):
        return self.nome

    def get_prezzo(self):
        return self.prezzo

    def get_quantita(self):
        return self.quantita

    def get_marca(self):
        return self.marca

    def get_codice(self):
        return self.codice

    def get_posizione(self):
        return self.posizione


    def set_nome(self, nuovo_nome):
        self.nome = nuovo_nome

    def set_prezzo(self, nuovo_prezzo):
        if nuovo_prezzo > 0:
            self.prezzo = nuovo_prezzo
        else:
            print("Il prezzo non può essere zero")

    def set_quantita(self, nuova_quantita):
        if nuova_quantita >= 0:
            self.quantita = nuova_quantita
        else:
             ValueError("La quantità non può essere negativa")

    def set_marca(self, nuova_marca):
        self.marca = nuova_marca


    def set_posizione(self, livello,scaffale,sezione):
        self.posizione = Posizione(livello,scaffale,sezione)

    def __str__(self):
        posizione_str = self.posizione if self.posizione else "non assegnata"
        return (f"[Codice: {self.codice}] {self.nome} ({self.marca}) "
                f"- €{self.prezzo} - {self.quantita} pezzi - {posizione_str}")


