from moduli.Documento import Documento

class Cliente:
    def __init__(self,codice,nome,indirizzo,telefono,email):
        self.indirizzo=indirizzo
        self.nome = nome
        self.email = email
        self.telefono = telefono
        self.codice=codice
        self.documenti=[] # Lista di oggetti Documento associati


    def get_codice(self):
          return self.codice

    def get_nome(self):
          return self.nome

    def get_indirizzo(self):
          return self.indirizzo

    def get_email(self):
          return self.email

    def get_telefono(self):
          return self.telefono

    def get_documenti(self):
          return self.documenti


    def set_nome(self,nuovo_nome):
        self.nome=nuovo_nome

    def set_indirizzo(self,nuovo_indirizzo):
        self.indirizzo=nuovo_indirizzo

    def set_email(self,nuovo_email):
        self.email=nuovo_email

    def set_telefono(self,nuovo_telefono):
        self.telefono=nuovo_telefono

    def set_documenti(self,nuovi_documenti):
        if isinstance(nuovi_documenti,Documento):
           self.documenti.append(nuovi_documenti)



    def __str__(self):
        return f"Cliente({self.codice}, {self.nome}, {self.indirizzo}, {self.telefono}, {self.email})"