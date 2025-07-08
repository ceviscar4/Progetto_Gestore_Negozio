from Controller.ControllerDipendenti import ControllerDipendenti
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, \
    QStackedWidget, QCheckBox, QDesktopWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from viste import VistaHome


class DipendenteGUI(QWidget):
    def __init__(self,main_gui):
        super().__init__()
        self.main_gui = main_gui
        self.controller = ControllerDipendenti()
        self.init_ui()
        self.center()


    def init_ui(self):
        self.setWindowTitle("Gestione Dipendenti")
        self.setGeometry(100,100,600,500)
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

        self.label_titolo = QLabel("GESTIONE DIPENDENTI")
        self.label_titolo.setFont(QFont("Arial", 16, QFont.Bold))
        self.label_titolo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_titolo)

        # Spacer sopra per centrare verticalmente
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Layout per i pulsanti centrati
        button_layout = QVBoxLayout()
        button_layout.setSpacing(5)  # Spaziatura uniforme tra i pulsanti
        button_layout.setContentsMargins(0, 0, 0, 0)  # Nessun margine extra

        # Pulsanti con dimensioni uniformi
        button_size = (200, 40)  # Larghezza 200px, Altezza 40px

        self.btn_aggiungi = QPushButton("Aggiungi Dipendente")
        self.btn_aggiungi.setFixedSize(*button_size)
        self.btn_aggiungi.setStyleSheet(self.button_style())
        self.btn_aggiungi.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_aggiungi))
        layout.addWidget(self.btn_aggiungi,alignment=Qt.AlignCenter)

        self.btn_modifica = QPushButton("Modifica Dipendente")
        self.btn_modifica.setFixedSize(*button_size)
        self.btn_modifica.setStyleSheet(self.button_style())
        self.btn_modifica.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_modifica))
        layout.addWidget(self.btn_modifica,alignment=Qt.AlignCenter)

        self.btn_rimuovi = QPushButton("Rimuovi Dipendente")
        self.btn_rimuovi.setFixedSize(*button_size)
        self.btn_rimuovi.setStyleSheet(self.button_style())
        self.btn_rimuovi.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_rimuovi))
        layout.addWidget(self.btn_rimuovi,alignment=Qt.AlignCenter)

        self.btn_visualizza = QPushButton("Visualizza Dipendenti")
        self.btn_visualizza.setFixedSize(*button_size)
        self.btn_visualizza.setStyleSheet(self.button_style())
        self.btn_visualizza.clicked.connect(lambda: self.stack.setCurrentWidget (self.page_visualizza))
        layout.addWidget(self.btn_visualizza,alignment=Qt.AlignCenter)


        self.btn_ricerca = QPushButton("Ricerca Dipendente")
        self.btn_ricerca.setFixedSize(*button_size)
        self.btn_ricerca.setStyleSheet(self.button_style())
        self.btn_ricerca.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_ricerca))
        layout.addWidget(self.btn_ricerca,alignment=Qt.AlignCenter)

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
        self.input_codice.setPlaceholderText("Codice Dipendente")
        self.input_codice.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice)

        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Nome Dipendente")
        self.input_nome.setStyleSheet(self.input_style())
        layout.addWidget(self.input_nome)

        self.input_mansione = QLineEdit()
        self.input_mansione.setPlaceholderText("Mansione Dipendente")
        self.input_mansione.setStyleSheet(self.input_style())
        layout.addWidget(self.input_mansione)

        self.input_telefono = QLineEdit()
        self.input_telefono.setPlaceholderText("Telefono Dipendente")
        self.input_telefono.setStyleSheet(self.input_style())
        layout.addWidget(self.input_telefono)

        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Email Dipendente")
        self.input_email.setStyleSheet(self.input_style())
        layout.addWidget(self.input_email)

        self.btn_conferma_aggiungi = QPushButton("Conferma")
        self.btn_conferma_aggiungi.setStyleSheet(self.button_style())
        self.btn_conferma_aggiungi.clicked.connect(self.aggiungi_dipendente)
        layout.addWidget(self.btn_conferma_aggiungi)

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
        self.input_codice_mod.setPlaceholderText("Codice Dipendente")
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

        self.input_mansione_mod = QLineEdit()
        self.input_mansione_mod.setPlaceholderText("Nuova mansione")
        self.input_mansione_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_mansione_mod)

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
        self.btn_conferma_modifica.clicked.connect(self.modifica_dipendente)
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
        self.input_codice_rimuovi.setPlaceholderText("Codice Dipendente")
        self.input_codice_rimuovi.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice_rimuovi)

        self.btn_conferma_rimuovi = QPushButton("Conferma Rimuovi")
        self.btn_conferma_rimuovi.setStyleSheet(self.button_style())
        self.btn_conferma_rimuovi.clicked.connect(self.rimuovi_dipendente)
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

        self.input_ricerca = QLineEdit()
        self.input_ricerca.setPlaceholderText("Inserisci il nome del dipendente")
        self.input_ricerca.setStyleSheet(self.input_style())
        layout.addWidget(self.input_ricerca)

        self.btn_ricerca = QPushButton("Cerca")
        self.btn_ricerca.setStyleSheet(self.button_style())
        self.btn_ricerca.clicked.connect(self.ricerca_dipendente)
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

        self.chekbox_ordinati = QCheckBox("Ordina per nome")
        layout.addWidget(self.chekbox_ordinati)

        self.btn_visualizza = QPushButton("Visualizza")
        self.btn_visualizza.setStyleSheet(self.button_style())
        self.btn_visualizza.clicked.connect(lambda: self.visualizza_dipendenti(self.chekbox_ordinati.isChecked()))
        self.btn_visualizza.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_visualizza)

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

    def aggiungi_dipendente(self):
        codice = self.input_codice.text()
        nome = self.input_nome.text()
        mansione = self.input_mansione.text()
        telefono = self.input_telefono.text()
        email = self.input_email.text()
        if codice and nome and mansione and telefono and email:
            try:
                telefono = int(telefono)
                self.controller.aggiungi_dipendenti(codice, nome, mansione, telefono, email)
                self.output.append(f"✅ Dipendente: {nome}, codice: {codice} aggiunto correttamente!")
            except ValueError:
                self.output.append(f"⚠️ Telefono deve essere numerico!")
        else:
            self.output.append("⚠️ Inserisci tutti i dati del dipendente!")
        self.stack.setCurrentWidget(self.home)


    def modifica_dipendente(self):
        codice_mod = self.input_codice_mod.text()
        nome = self.input_nome_mod.text()
        nuovo_nome = self.input_nuovo_nome.text()
        nuova_mansione = self.input_mansione_mod.text()
        nuovo_telefono = self.input_telefono_mod.text()
        nuova_email = self.input_email_mod.text()
        if codice_mod and nome and nuovo_nome and nuova_mansione and nuovo_telefono and nuova_email:
            try:
                nuovo_telefono = int(nuovo_telefono)
                nuova_mansione = str(nuova_mansione)
                self.controller.modifica_dipendenti(codice_mod, nome, nuovo_nome, nuova_mansione, nuovo_telefono, nuova_email)
                self.output.append(f"✅ Dipendente: {nome}, codice: {codice_mod} modificato con successo!")
            except ValueError:
                self.output.append(f"⚠️ telefono deve essere numerico o mansione non deve essere numerica!")
        else:
            self.output.append(f"⚠️ Tutti i dati del dipendente devono essere inseriti!")
        self.stack.setCurrentWidget(self.home)

    def rimuovi_dipendente(self):
        codice_rimuovi = self.input_codice_rimuovi.text()
        if codice_rimuovi:

               self.controller.rimuovi_dipendenti(codice_rimuovi)
               self.output.append(f"Dipendente: {codice_rimuovi} rimosso con successo!")
        else:
            self.output.append(f"Inserisci tutti i dati del dipendente!")
        self.stack.setCurrentWidget(self.home)


    def ricerca_dipendente(self):
        nome_ricerca = self.input_ricerca.text()
        if nome_ricerca:
            dipendenti = self.controller.ricerca_dipendenti(nome_ricerca)
            self.output.clear()
            if dipendenti:
                for dipendente in dipendenti:
                    self.output.append(f"🔍 codice: {dipendente.nome}, nome: {dipendente.nome}, mansione: {dipendente.mansione}, telefono: {dipendente.telefono}, email: {dipendente.email} ")

            else:
                self.output.append("Nessun dipendente trovato!")

        else:
            self.output.append("Inserisci il nome del dipendente!")
        self.stack.setCurrentWidget(self.home)

    def visualizza_dipendenti(self, ordinati=False):
        self.output.clear()
        dipendenti = self.controller.gestione_dipendenti.dipendenti
        if dipendenti:
            lista_dipendenti= sorted(dipendenti.values(), key=lambda x: x.nome) if ordinati else dipendenti.values()
            for x in lista_dipendenti:
                self.output.append(
                    f"📦 Codice: {x.codice} - Nome: {x.nome} - mansione: {x.mansione} - telefono: {x.telefono} - email: {x.email}")

        else:
            self.output.append("Nessun dipendente trovato!")
        self.stack.setCurrentWidget(self.home)

    def back_to_gestione(self):
            # Usa il riferimento alla GUI principale per cambiare il widget corrente
            self.main_gui.stack.setCurrentWidget(self.main_gui.gestione)



















