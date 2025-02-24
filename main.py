from Login.Login import Login

if __name__ == '__main__':

    accesso = Login()

    # Registrazione
    print("\n=== REGISTRAZIONE ===")
    password = input("Scegli una password: ")
    id_utente = accesso.registra_utente(password)

    # Tentativo di login
    print("\n=== LOGIN ===")
    id_input = input("Inserisci il tuo ID: ")
    pass_input = input("Inserisci la password: ")

    accesso.login(id_input, pass_input)
