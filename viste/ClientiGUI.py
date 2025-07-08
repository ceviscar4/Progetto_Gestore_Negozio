from Controller.ControllerClienti import ControllerClienti
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, \
    QStackedWidget, QCheckBox, QDesktopWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from viste import VistaHome

class ClientiGUI(QWidget):
    def __init__(self,main_gui):
        super().__init__()
        self.main_gui = main_gui
        self.controller = ControllerClienti()
        self.init_ui()
        self.center()


    def init_ui(self):
        self.setWindowTitle("Gestione Clienti")
        self.setGeometry(100,100,500,400)
        self.setStyleSheet("background-color: #f4f4f4;")

        self.stack = QStackedWidget()
        self.layout_principale = QVBoxLayout(self)
        self.layout_principale.addWidget(self.stack)

        self.init_home()
        self.init_aggiungi()
        self.init_modifica()
        self.init_rimuovi()
        self.init_ricerca()
        self.init_visualizza()

        self.setLayout(self.layout_principale)

    def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

    def init_home(self):
        self.home = QWidget()
        layout = QVBoxLayout(self.home)

        # Layout secondario per contenere i pulsanti
        button_layout = QVBoxLayout()
        button_layout.setSpacing(3)  # Riduci lo spazio tra i pulsanti
        button_layout.setContentsMargins(0, 0, 0, 0)  # Nessun margine

        self.titolo = QLabel("GESTIONE CLIENTI")
        self.titolo.setFont(QFont("Arial", 16, QFont.Bold))
        self.titolo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.titolo)

        # Spacer sopra per centrare verticalmente
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Layout per i pulsanti centrati
        button_layout = QVBoxLayout()
        button_layout.setSpacing(5)  # Spaziatura uniforme tra i pulsanti
        button_layout.setContentsMargins(0, 0, 0, 0)  # Nessun margine extra

        # Pulsanti con dimensioni uniformi
        button_size = (200, 40)  # Larghezza 200px, Altezza 40px

        self.btn_aggiungi = QPushButton("Aggiungi Cliente")
        self.btn_aggiungi.setFixedSize(*button_size)
        self.btn_aggiungi.setStyleSheet(self.button_style())
        self.btn_aggiungi.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_aggiungi))
        layout.addWidget(self.btn_aggiungi,alignment=Qt.AlignCenter)


        self.btn_modifica = QPushButton("Modifica Cliente")
        self.btn_modifica.setFixedSize(*button_size)
        self.btn_modifica.setStyleSheet(self.button_style())
        self.btn_modifica.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_modifica))
        layout.addWidget(self.btn_modifica,alignment=Qt.AlignCenter)

        self.btn_rimuovi = QPushButton("Rimuovi Cliente")
        self.btn_rimuovi.setFixedSize(*button_size)
        self.btn_rimuovi.setStyleSheet(self.button_style())
        self.btn_rimuovi.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_rimuovi))
        layout.addWidget(self.btn_rimuovi,alignment=Qt.AlignCenter)

        self.btn_ricerca = QPushButton("Ricerca Cliente")
        self.btn_ricerca.setFixedSize(*button_size)
        self.btn_ricerca.setStyleSheet(self.button_style())
        self.btn_ricerca.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_ricerca))
        layout.addWidget(self.btn_ricerca,alignment=Qt.AlignCenter)

        self.btn_visualizza = QPushButton("Visualizza Clienti")
        self.btn_visualizza.setFixedSize(*button_size)
        self.btn_visualizza.setStyleSheet(self.button_style())
        self.btn_visualizza.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_visualizza))
        layout.addWidget(self.btn_visualizza,alignment=Qt.AlignCenter)

        self.btn_back = QPushButton("Torna alla Gestione")
        self.btn_back.setFixedSize(*button_size)
        self.btn_back.setStyleSheet(self.button_style())
        self.btn_back.clicked.connect(self.back_to_gestione)
        layout.addWidget(self.btn_back,alignment=Qt.AlignCenter)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: white; border-radius: 8px; padding: 5px;")
        layout.addWidget(self.output)

        # Aggiungi il layout dei pulsanti al layout principale
        layout.addLayout(button_layout)

        # Spacer sotto per centrare verticalmente
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))


        self.stack.addWidget(self.home)

    def init_aggiungi(self):
        self.page_aggiungi = QWidget()
        layout = QVBoxLayout()

        self.input_codice = QLineEdit()
        self.input_codice.setPlaceholderText("Codice Cliente")
        self.input_codice.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice)

        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Nome Cliente")
        self.input_nome.setStyleSheet(self.input_style())
        layout.addWidget(self.input_nome)

        self.input_indirizzo = QLineEdit()
        self.input_indirizzo.setPlaceholderText("Indirizzo Cliente")
        self.input_indirizzo.setStyleSheet(self.input_style())
        layout.addWidget(self.input_indirizzo)

        self.input_telefono = QLineEdit()
        self.input_telefono.setPlaceholderText("Telefono Cliente")
        self.input_telefono.setStyleSheet(self.input_style())
        layout.addWidget(self.input_telefono)

        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Email Cliente")
        self.input_email.setStyleSheet(self.input_style())
        layout.addWidget(self.input_email)

        self.btn_conferma = QPushButton("Aggiungi")
        self.btn_conferma.setStyleSheet(self.button_style())
        self.btn_conferma.clicked.connect(lambda: self.stack.setCurrentWidget(self.aggiungi_cliente()))
        layout.addWidget(self.btn_conferma)

        self.btn_back = QPushButton("Indietro")
        self.btn_back.setStyleSheet(self.button_style())
        self.btn_back.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back)

        self.page_aggiungi.setLayout(layout)
        self.stack.addWidget(self.page_aggiungi)

    def init_modifica(self):
        self.page_modifica = QWidget()
        layout = QVBoxLayout()

        self.input_codice_mod = QLineEdit()
        self.input_codice_mod.setPlaceholderText("Codice Cliente")
        self.input_codice_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice_mod)

        self.input_nome_mod = QLineEdit()
        self.input_nome_mod.setPlaceholderText("Nome attuale")
        self.input_nome_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_nome_mod)

        self.input_nuovo_nome = QLineEdit()
        self.input_nuovo_nome.setPlaceholderText("Nuovo nome")
        self.input_nuovo_nome.setStyleSheet(self.input_style())
        layout.addWidget(self.input_nuovo_nome)

        self.input_indirizzo_mod = QLineEdit()
        self.input_indirizzo_mod.setPlaceholderText("Nuovo indirizzo")
        self.input_indirizzo_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_indirizzo_mod)

        self.input_telefono_mod = QLineEdit()
        self.input_telefono_mod.setPlaceholderText("Nuovo telefono")
        self.input_telefono_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_telefono_mod)

        self.input_email_mod = QLineEdit()
        self.input_email_mod.setPlaceholderText("Nuova email")
        self.input_email_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_email_mod)

        self.btn_conferma_modifica = QPushButton("Conferma Modifica")
        self.btn_conferma_modifica.setStyleSheet(self.button_style())
        self.btn_conferma_modifica.clicked.connect(self.modifica_cliente)
        layout.addWidget(self.btn_conferma_modifica)

        self.btn_back_mod = QPushButton("Indietro")
        self.btn_back_mod.setStyleSheet(self.button_style())
        self.btn_back_mod.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_mod)

        self.page_modifica.setLayout(layout)
        self.stack.addWidget(self.page_modifica)

    def init_rimuovi(self):
        self.page_rimuovi = QWidget()
        layout = QVBoxLayout()

        self.input_codice_rimuovi = QLineEdit()
        self.input_codice_rimuovi.setPlaceholderText("Codice Cliente")
        self.input_codice_rimuovi.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice_rimuovi)

        self.btn_conferma_rimuovi = QPushButton("Conferma Rimuovi")
        self.btn_conferma_rimuovi.setStyleSheet(self.button_style())
        self.btn_conferma_rimuovi.clicked.connect(self.rimuovi_cliente)
        layout.addWidget(self.btn_conferma_rimuovi)

        self.btn_back_rimuovi = QPushButton("Indietro")
        self.btn_back_rimuovi.setStyleSheet(self.button_style())
        self.btn_back_rimuovi.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_rimuovi)

        self.page_rimuovi.setLayout(layout)
        self.stack.addWidget(self.page_rimuovi)

    def init_ricerca(self):
        self.page_ricerca = QWidget()
        layout = QVBoxLayout()

        self.input_nome_ricerca = QLineEdit()
        self.input_nome_ricerca.setPlaceholderText("Inserisci il nome del cliente")
        self.input_nome_ricerca.setStyleSheet(self.input_style())
        layout.addWidget(self.input_nome_ricerca)

        self.btn_ricerca = QPushButton("Cerca")
        self.btn_ricerca.setStyleSheet(self.button_style())
        self.btn_ricerca.clicked.connect(self.ricerca_cliente)
        layout.addWidget(self.btn_ricerca)

        self.btn_back_ricerca = QPushButton("Indietro")
        self.btn_back_ricerca.setStyleSheet(self.button_style())
        self.btn_back_ricerca.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_ricerca)

        self.page_ricerca.setLayout(layout)
        self.stack.addWidget(self.page_ricerca)

    def init_visualizza(self):
        self.page_visualizza = QWidget()
        layout = QVBoxLayout()

        self.chekbox_ordinati = QCheckBox("Ordinati per nome")
        layout.addWidget(self.chekbox_ordinati)

        self.btn_ricerca_visualizza = QPushButton("Visualizza")
        self.btn_ricerca_visualizza.setStyleSheet(self.button_style())
        self.btn_ricerca_visualizza.clicked.connect(lambda: self.visualizza_clienti(self.chekbox_ordinati.isChecked()))
        self.btn_ricerca_visualizza.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_ricerca_visualizza)

        self.btn_back_visualizza = QPushButton("Indietro")
        self.btn_back_visualizza.setStyleSheet(self.button_style())
        self.btn_back_visualizza.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_visualizza)

        self.page_visualizza.setLayout(layout)
        self.stack.addWidget(self.page_visualizza)

    def button_style(self):
        return "QPushButton {background-color: #007BFF; color: white; border-radius: 10px; padding: 10px; font-size: 14px;} QPushButton:hover {background-color: #0056b3;}"

    def input_style(self):
        return "QLineEdit {border: 2px solid #ccc; border-radius: 10px; padding: 5px; font-size: 14px; background-color: white;}"

    def aggiungi_cliente(self):
        codice = self.input_codice.text()
        nome = self.input_nome.text()
        indirizzo = self.input_indirizzo.text()
        telefono = self.input_telefono.text()
        email = self.input_email.text()
        if codice and nome and indirizzo and telefono and email:
            try:
                telefono = int(telefono)
                nome = str(nome)

                self.controller.aggiungi_cliente(codice, nome, indirizzo, telefono, email)
                self.output.append(f"✅ Cliente: {nome}, codice: {codice} aggiunto correttamente!")
            except ValueError:
                self.output.append("telefono deve essere un numerico e nome deve essere una stringa!")
        else:
            self.output.append("Inserire tutti i campi!")
        self.stack.setCurrentWidget(self.home)

    def modifica_cliente(self):
        codice = self.input_codice_mod.text()
        nome_attuale = self.input_nome_mod.text()
        nome_nuovo = self.input_nuovo_nome.text()
        indirizzo_nuovo = self.input_indirizzo_mod.text()
        telefono_nuovo = self.input_telefono_mod.text()
        email_nuovo = self.input_email_mod.text()
        if codice and nome_attuale and nome_nuovo and indirizzo_nuovo and telefono_nuovo and email_nuovo:
            try:
                telefono_nuovo = int(telefono_nuovo)
                nome_nuovo = str(nome_nuovo)
                nome_attuale = str(nome_attuale)
                self.controller.modifica_cliente(codice, nome_attuale, nome_nuovo, indirizzo_nuovo, telefono_nuovo, email_nuovo)
                self.output.append(f"Cliente: {nome_attuale} modificato correttamente!")
            except ValueError:
                self.output.append("telefono deve essere numerico o nome deve essere una stringa!")
        else:
            self.output.append("Inserire tutti i campi!")
        self.stack.setCurrentWidget(self.home)


    def rimuovi_cliente(self):
        codice = self.input_codice_rimuovi.text()
        if codice in self.controller.gestione_clienti.clienti:
            try:
               self.controller.rimuovi_cliente(codice)
               self.output.append(f"Cliente: {codice} rimosso correttamente!")
            except ValueError:
                self.output.append("Codice non valido!")
        else:
            self.output.append("Cliente non presente!")
        self.stack.setCurrentWidget(self.home)

    def ricerca_cliente(self):
        nome = self.input_nome_ricerca.text()
        if not nome:
            self.output.append("Inserire il nome del cliente!")
            return
        if nome.isdigit():
            self.output.append("Nome non valido! Inserisci una stringa non numerica.")
            self.stack.setCurrentWidget(self.home)
            return

        risultati = [p for p in self.controller.gestione_clienti.clienti.values() if nome.lower() in p.nome.lower()]

        self.output.clear()

        if risultati:
            for p in risultati:
                self.output.append(
                    f"🔍 codice: {p.codice}, nome: {p.nome}, indirizzo: {p.indirizzo}, telefono: {p.telefono}, email: {p.email}")
        else:
            self.output.append("Nessun cliente trovato!")

        self.stack.setCurrentWidget(self.home)
        # self.controller.ricerca_cliente(nome)
                #self.output.append(f"Cliente: {nome} trovato correttamente!")
           # except ValueError:
                #self.output.append("Nome non valido!")
        #else:
            #self.output.append("Inserire il nome del cliente!")


    def visualizza_clienti(self, ordinati= False):
        self.output.clear()
        clienti = self.controller.gestione_clienti.clienti
        if clienti:
            lista_clienti = sorted(clienti.values(), key=lambda x: x.nome) if ordinati else clienti.values()
            for x in lista_clienti:
                self.output.append(f"📦 Codice: {x.codice} - Nome: {x.nome} - indirizzo: {x.indirizzo} - telefono: {x.telefono} - email: {x.email}")
        else:
            self.output.append("Nessun cliente trovato!")
        self.stack.setCurrentWidget(self.home)

    def back_to_gestione(self):
            # Usa il riferimento alla GUI principale per cambiare il widget corrente
            self.main_gui.stack.setCurrentWidget(self.main_gui.gestione)


