from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, \
    QStackedWidget, QCheckBox, QDesktopWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from viste import VistaHome
from Controller.ControllerMagazzino import ControllerMagazzino


class MagazzinoGUI(QWidget):
    def __init__(self, main_gui):
        super().__init__()
        self.main_gui = main_gui
        self.controller = ControllerMagazzino()
        self.init_ui()
        self.center()


    def init_ui(self):
        self.setWindowTitle("Gestione Magazzino")
        self.setGeometry(100, 100, 600, 500)
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

        # Layout principale per centrare i pulsanti nella pagina
        layout = QVBoxLayout(self.home)  # Imposta direttamente il layout alla pagina 'gestione'

        # Layout secondario per contenere i pulsanti
        button_layout = QVBoxLayout()
        button_layout.setSpacing(3)  # Riduci lo spazio tra i pulsanti
        button_layout.setContentsMargins(0, 0, 0, 0)  # Nessun margine

        self.label_titolo = QLabel("GESTIONE MAGAZZINO")
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

        self.btn_aggiungi = QPushButton("Aggiungi Prodotto")
        self.btn_aggiungi.setFixedSize(*button_size)
        self.btn_aggiungi.setStyleSheet(self.button_style())
        self.btn_aggiungi.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_aggiungi))
        layout.addWidget(self.btn_aggiungi,alignment=Qt.AlignCenter)

        self.btn_modifica = QPushButton("Modifica Prodotto")
        self.btn_modifica.setFixedSize(*button_size)
        self.btn_modifica.setStyleSheet(self.button_style())
        self.btn_modifica.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_modifica))
        layout.addWidget(self.btn_modifica,alignment=Qt.AlignCenter)

        self.btn_rimuovi = QPushButton("Rimuovi Prodotto")
        self.btn_rimuovi.setFixedSize(*button_size)
        self.btn_rimuovi.setStyleSheet(self.button_style())
        self.btn_rimuovi.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_rimuovi))
        layout.addWidget(self.btn_rimuovi,alignment=Qt.AlignCenter)

        self.btn_visualizza = QPushButton("Visualizza Prodotti")
        self.btn_visualizza.setFixedSize(*button_size)
        self.btn_visualizza.setStyleSheet(self.button_style())
        self.btn_visualizza.clicked.connect(lambda: self.visualizza_prodotti())
        layout.addWidget(self.btn_visualizza,alignment=Qt.AlignCenter)

        self.btn_ricerca = QPushButton("Ricerca Prodotto")
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
        self.input_codice.setPlaceholderText("Codice Prodotto")
        self.input_codice.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice)

        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Nome Prodotto")
        self.input_nome.setStyleSheet(self.input_style())
        layout.addWidget(self.input_nome)

        self.input_marca = QLineEdit()
        self.input_marca.setPlaceholderText("Marca Prodotto")
        self.input_marca.setStyleSheet(self.input_style())
        layout.addWidget(self.input_marca)

        self.input_prezzo = QLineEdit()
        self.input_prezzo.setPlaceholderText("Prezzo Prodotto")
        self.input_prezzo.setStyleSheet(self.input_style())
        layout.addWidget(self.input_prezzo)

        self.input_quantita = QLineEdit()
        self.input_quantita.setPlaceholderText("Quantità Prodotto")
        self.input_quantita.setStyleSheet(self.input_style())
        layout.addWidget(self.input_quantita)

        self.btn_conferma_aggiungi = QPushButton("Conferma")
        self.btn_conferma_aggiungi.setStyleSheet(self.button_style())
        self.btn_conferma_aggiungi.clicked.connect(self.aggiungi_prodotto)
        layout.addWidget(self.btn_conferma_aggiungi)

        self.btn_back_aggiungi = QPushButton("Indietro")
        self.btn_back_aggiungi.setStyleSheet(self.button_style())
        self.btn_back_aggiungi.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_aggiungi)


        self.page_aggiungi.setLayout(layout)
        self.stack.addWidget(self.page_aggiungi)

    def init_modifica(self):
        self.page_modifica = QWidget()
        layout = QVBoxLayout()

        self.input_codice_mod = QLineEdit()
        self.input_codice_mod.setPlaceholderText("Codice Prodotto")
        self.input_codice_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice_mod)

        self.input_nome_mod = QLineEdit()
        self.input_nome_mod.setPlaceholderText("Nuovo Nome")
        self.input_nome_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_nome_mod)

        self.input_prezzo_mod = QLineEdit()
        self.input_prezzo_mod.setPlaceholderText("Nuovo Prezzo")
        self.input_prezzo_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_prezzo_mod)

        self.input_quantita_mod = QLineEdit()
        self.input_quantita_mod.setPlaceholderText("Nuova Quantità")
        self.input_quantita_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_quantita_mod)

        self.btn_conferma_modifica = QPushButton("Conferma Modifica")
        self.btn_conferma_modifica.setStyleSheet(self.button_style())
        self.btn_conferma_modifica.clicked.connect(self.modifica_prodotto)
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

        self.input_codice_rim = QLineEdit()
        self.input_codice_rim.setPlaceholderText("Codice Prodotto")
        self.input_codice_rim.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice_rim)

        self.btn_conferma_rimuovi = QPushButton("Conferma Rimozione")
        self.btn_conferma_rimuovi.setStyleSheet(self.button_style())
        self.btn_conferma_rimuovi.clicked.connect(self.rimuovi_prodotto)
        layout.addWidget(self.btn_conferma_rimuovi)

        self.btn_back_rim = QPushButton("Indietro")
        self.btn_back_rim.setStyleSheet(self.button_style())
        self.btn_back_rim.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_rim)

        self.page_rimuovi.setLayout(layout)
        self.stack.addWidget(self.page_rimuovi)

    def init_ricerca(self):
        self.page_ricerca = QWidget()
        layout = QVBoxLayout()

        self.input_nome_ricerca = QLineEdit()
        self.input_nome_ricerca.setPlaceholderText("Nome Prodotto")
        self.input_nome_ricerca.setStyleSheet(self.input_style())
        layout.addWidget(self.input_nome_ricerca)

        self.btn_conferma_ricerca = QPushButton("Cerca")
        self.btn_conferma_ricerca.clicked.connect(self.ricerca_prodotto)
        self.btn_conferma_ricerca.setStyleSheet(self.button_style())

        layout.addWidget(self.btn_conferma_ricerca)

        self.btn_back_ricerca = QPushButton("Indietro")
        self.btn_back_ricerca.setStyleSheet(self.button_style())
        self.btn_back_ricerca.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_ricerca)

        self.page_ricerca.setLayout(layout)
        self.stack.addWidget(self.page_ricerca)



    def init_visualizza(self):
        self.page_visualizza = QWidget()
        layout = QVBoxLayout()

        self.checkbox_ordinati = QCheckBox("Ordina per nome")
        layout.addWidget(self.checkbox_ordinati)


        self.btn_conferma_visualizza = QPushButton("Visualizza Prodotti")
        self.btn_conferma_visualizza.setStyleSheet(self.button_style())
        self.btn_conferma_visualizza.clicked.connect(lambda: self.visualizza_prodotti(self.checkbox_ordinati.isChecked()))
        self.btn_visualizza.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_visualizza))

        layout.addWidget(self.btn_conferma_visualizza)

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

    def aggiungi_prodotto(self):
        codice = self.input_codice.text()
        nome = self.input_nome.text()
        marca = self.input_marca.text()
        prezzo = self.input_prezzo.text()
        quantita = self.input_quantita.text()

        if codice and nome and marca and prezzo and quantita:
            try:
                prezzo = float(prezzo)
                quantita = int(quantita)
                self.controller.aggiungi_prodotto(codice, nome, prezzo, marca, quantita)
                self.output.append(f"✅ Prodtto: {nome}, codice: {codice} aggiunto!")
            except  ValueError:
                self.output.append(f"⚠️ Prezzo e quantità devono essere numerici!")
        else:
            self.output.append("⚠️ Inserisci tutti i dati del prodotto!")
        self.stack.setCurrentWidget(self.home)


    def modifica_prodotto(self):
        codice = self.input_codice_mod.text()
        nome = self.input_nome_mod.text()
        prezzo = self.input_prezzo_mod.text()
        quantita = self.input_quantita_mod.text()

        if codice and nome and prezzo and quantita:
            try:
                prezzo = float(prezzo)
                quantita = int(quantita)
                self.controller.modifica_prodotto(codice, nome, prezzo, quantita)
                self.output.append(f"✅ Prodtto {nome} modificato!")
            except ValueError:
                self.output.append(f"⚠️ prezzo e quantità devono essere numerici!")

        else:
            self.output.append("⚠️ Inserisci tutti i dati del prodotto!")
        self.stack.setCurrentWidget(self.home)


    def rimuovi_prodotto(self):
        codice = self.input_codice_rim.text()

        if codice in self.controller.gestore_magazzino.prodotti.keys():
            try:
                self.controller.rimuovi_prodotto(codice)
                self.output.append(f" Prodotto {codice} rimosso!")
            except ValueError:
                self.output.append("Il codice deve essere numerico!")
        else:
            self.output.append("Il prodotto non è presente !")
        self.stack.setCurrentWidget(self.home)



    def ricerca_prodotto(self):
        nome = self.input_nome_ricerca.text()
        if nome:
            risultati = [p for p in self.controller.gestore_magazzino.prodotti.values() if nome.lower() in p.nome.lower()]
            self.output.clear()
            if risultati:
                for p in risultati:
                    self.output.append(f"🔍 {p.nome} - {p.codice} - {p.marca} - {p.prezzo}0€ - {p.quantita} pezzi")

            else:
                self.output.append("Nessun prodotto trovato!")

        else:
            self.output.append("Inserisci il nome del prodotto da ricercare!")
        self.stack.setCurrentWidget(self.home)

    def visualizza_prodotti(self, ordinati = False):
        self.output.clear()
        prodotti = self.controller.gestore_magazzino.prodotti
        if prodotti:
            lista_prodotti= sorted(prodotti.values(), key=lambda x: x.nome) if ordinati else prodotti.values()
            for x in lista_prodotti:
                self.output.append(f"📦 Codice: {x.codice} - Nome: {x.nome} - Marca: {x.marca} - Prezzo: {x.prezzo}0€ - Quantità: {x.quantita} pezzi")
        else:
            self.output.append("Nessun prodotto presente!")

        self.stack.setCurrentWidget(self.home)

    def back_to_gestione(self):
        # Usa il riferimento alla GUI principale per cambiare il widget corrente
        self.main_gui.stack.setCurrentWidget(self.main_gui.gestione)


