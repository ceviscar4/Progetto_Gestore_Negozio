


class Dipendenti:
    def __init__(self,codice,nome,mansione,telefono,email):
        self.codice=codice
        self.nome=nome
        self.mansione=mansione
        self.telefono=telefono
        self.email=email

    def get_codice(self):
        return self.codice

    def get_nome(self):
        return self.nome

    def get_mansione(self):
        return self.mansione

    def get_telefono(self):
        return self.telefono

    def get_email(self):
        return self.email

    def set_nome(self,nuovo_nome):
        self.nome=nuovo_nome

    def set_mansione(self,nuova_mansione):
        if not self.mansione:
            print("Il dipendente non ha una mansione attuale")
        else:
            self.mansione=nuova_mansione

    def set_telefono(self,nuovo_telefono):
        self.telefono=nuovo_telefono

    def set_email(self,nuova_email):
        self.email=nuova_email

    def __str__(self):
        return f"Dipendente({self.codice}, {self.nome}, {self.mansione}, {self.telefono}, {self.email})"