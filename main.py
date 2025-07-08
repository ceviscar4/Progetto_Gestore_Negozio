import sys

from PyQt5.QtWidgets import QApplication

from Login.Login import Login
from viste.ClientiGUI import ClientiGUI
from viste.DipendentiGUI import DipendenteGUI

#from viste.MagazzinoGUI import MagazzinoGUI
from viste.NuovoGUI import MagazzinoGUI
from viste.VistaHome import HomeGUI
from viste.DocumentoGUI import DocumentiGUI

if __name__ == '__main__':

    #accesso = Login()

    # Registrazione
    #print("\n=== REGISTRAZIONE ===")
    #password = input("Scegli una password: ")
    #id_utente = accesso.registra_utente(password)

    # Tentativo di login
    #print("\n=== LOGIN ===")
    #id_input = input("Inserisci il tuo ID: ")
    #pass_input = input("Inserisci la password: ")

   # accesso.login(id_input, pass_input)

   # app = QApplication([])
    #window = MagazzinoGUI(main_gui = HomeGUI)
    #window.show()
    #app.exec_()



    app = QApplication([])
    window = HomeGUI()
    window.show()
    sys.exit(app.exec_())