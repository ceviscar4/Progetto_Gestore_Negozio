


class Posizione:
    def __init__(self,livello,scaffale,sezione):
        self.livello = int(livello)
        self.scaffale = int(scaffale)
        self.sezione = str(sezione)


    def get_livello(self):
        return self.livello

    def get_scaffale(self):
        return self.scaffale

    def get_sezione(self):
        return self.sezione

    def set_livello(self,livello):
        if livello >= 0:
            self.livello = livello
        else:
            print("Il livello non può essere minore di 0")

    def set_scaffale(self,scaffale):
        if scaffale >= 0:
            self.scaffale = scaffale
        else:
            print("Lo scaffale non può essere minore di 0 ")

    def set_sezione(self,sezione):
        if sezione != "":
            self.sezione = sezione
        else:
            print("La sezione non può essere vuota")


    def __str__(self):
        return f"Livello: {self.livello} - Scaffale: {self.scaffale} - Sezione: {self.sezione}"

