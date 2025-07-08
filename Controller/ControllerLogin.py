from Login.Login import Login


class ControllerLogin:
    def __init__(self):
        self.login = Login

    def login(self,username,password):
        self.login.login(username,password)

    def registra_utente(self, password):
        self.login.registra_utente(password)

    def genera_id(self):
        self.login.genera_id()