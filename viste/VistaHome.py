from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, \
    QStackedWidget, QCheckBox, QDesktopWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
from viste import NuovoGUI
from viste import ClientiGUI
from viste import DipendentiGUI
from viste import DocumentoGUI
from Login.Login import Login



class HomeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.login = Login()
        self.DocumentiGUI = DocumentoGUI.DocumentiGUI(self)
        self.NuovoGUI = NuovoGUI.MagazzinoGUI(self)
        self.ClientiGUI = ClientiGUI.ClientiGUI(self)
        self.DipendentiGUI = DipendentiGUI.DipendenteGUI(self)

        self.init_ui()
        self.center()


        self.stack.addWidget(self.NuovoGUI)
        self.stack.addWidget(self.ClientiGUI)
        self.stack.addWidget(self.DipendentiGUI)
        self.stack.addWidget(self.DocumentiGUI)


    def init_ui(self):
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #f4f4f4;")

        self.stack = QStackedWidget()
        self.layout_principale = QVBoxLayout(self)
        self.layout_principale.addWidget(self.stack)


        self.init_home()
        self.init_gestione()
        self.init_login()
        self.init_registra()


        self.setLayout(self.layout_principale)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_home(self):
        self.home = QWidget()
        layout = QVBoxLayout()

        self.label_titolo = QLabel("LOGIN")
        self.label_titolo.setFont(QFont("Arial", 16, QFont.Bold))
        self.label_titolo.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.label_titolo)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.btn_login = QPushButton("Login")
        self.btn_login.setStyleSheet(self.button_style())
        self.btn_login.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_login))
        self.btn_login.setFixedSize(120, 40)  # Larghezza: 150 px, Altezza: 50 px


        layout.addWidget(self.btn_login, alignment=Qt.AlignCenter)

        self.btn_registra = QPushButton("Registra")
        self.btn_registra.setStyleSheet(self.button_style())
        self.btn_registra.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_registra))
        self.btn_registra.setFixedSize(150, 40)
        layout.addWidget(self.btn_registra, alignment=Qt.AlignCenter)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


        self.home.setLayout(layout)
        self.stack.addWidget(self.home)

    def init_login(self):
        self.page_login = QWidget()
        layout = QVBoxLayout()

        self.input_id= QLineEdit()
        self.input_id.setPlaceholderText("ID")
        self.input_id.setStyleSheet(self.input_style())
        layout.addWidget(self.input_id)

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Password")
        self.input_password.setStyleSheet(self.input_style())
        layout.addWidget(self.input_password)

        self.btn_conferma_login = QPushButton("Conferma")
        self.btn_conferma_login.setStyleSheet(self.button_style())
        self.btn_conferma_login.clicked.connect(self.gestione_login)
        layout.addWidget(self.btn_conferma_login)

        self.btn_back_login = QPushButton("Indietro")
        self.btn_back_login.setStyleSheet(self.button_style())
        self.btn_back_login.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_login)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: white; border-radius: 8px; padding: 5px;")
        layout.addWidget(self.output)

        self.page_login.setLayout(layout)
        self.stack.addWidget(self.page_login)


    def init_gestione(self):
        self.gestione = QWidget()

        # Layout principale per centrare i pulsanti nella pagina
        layout = QVBoxLayout(self.gestione)  # Imposta direttamente il layout alla pagina 'gestione'



        # Layout secondario per contenere i pulsanti
        button_layout = QVBoxLayout()
        button_layout.setSpacing(5)  # Riduci lo spazio tra i pulsanti
        button_layout.setContentsMargins(0, 0, 0, 0)  # Nessun margine

        self.label_titolo = QLabel("GESTIONE")
        self.label_titolo.setFont(QFont("Arial", 16, QFont.Bold))
        self.label_titolo.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.label_titolo, alignment=Qt.AlignHCenter)


        # Spacer sopra per centrare verticalmente
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Layout per i pulsanti centrati
        button_layout = QVBoxLayout()
        button_layout.setSpacing(5)  # Spaziatura uniforme tra i pulsanti
        button_layout.setContentsMargins(0, 0, 0, 0)  # Nessun margine extra

        # Pulsanti con dimensioni uniformi
        button_size = (200, 40)  # Larghezza 200px, Altezza 40px

        self.btn_gestione = QPushButton("Gestione Magazzino")
        self.btn_gestione.setFixedSize(*button_size)
        self.btn_gestione.setStyleSheet(self.button_style())
        self.btn_gestione.clicked.connect(lambda: self.stack.setCurrentWidget(self.NuovoGUI))
        button_layout.addWidget(self.btn_gestione, alignment=Qt.AlignCenter)


        self.btn_gestione_clienti = QPushButton("Gestione Clienti")
        self.btn_gestione_clienti.setFixedSize(*button_size)
        self.btn_gestione_clienti.setStyleSheet(self.button_style())
        self.btn_gestione_clienti.clicked.connect(lambda: self.stack.setCurrentWidget(self.ClientiGUI))
        button_layout.addWidget(self.btn_gestione_clienti,alignment=Qt.AlignCenter)


        self.btn_gestione_dipendenti = QPushButton("Gestione Dipendenti")
        self.btn_gestione_dipendenti.setFixedSize(*button_size)
        self.btn_gestione_dipendenti.setStyleSheet(self.button_style())
        self.btn_gestione_dipendenti.clicked.connect(lambda: self.stack.setCurrentWidget(self.DipendentiGUI))
        button_layout.addWidget(self.btn_gestione_dipendenti,alignment=Qt.AlignCenter)

        self.btn_gestione_documenti = QPushButton("Gestione Documenti")
        self.btn_gestione_documenti.setFixedSize(*button_size)
        self.btn_gestione_documenti.setStyleSheet(self.button_style())
        self.btn_gestione_documenti.clicked.connect(lambda: self.stack.setCurrentWidget(self.DocumentiGUI))
        button_layout.addWidget(self.btn_gestione_documenti,alignment=Qt.AlignCenter)

        self.btn_back_registra = QPushButton("Indietro a Registrazione")
        self.btn_back_registra.setFixedSize(*button_size)
        self.btn_back_registra.setStyleSheet(self.button_style())
        self.btn_back_registra.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_registra))
        button_layout.addWidget(self.btn_back_registra,alignment=Qt.AlignCenter)

        self.btn_back_login = QPushButton("Indietro a Login")
        self.btn_back_login.setFixedSize(*button_size)
        self.btn_back_login.setStyleSheet(self.button_style())
        self.btn_back_login.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_login))
        button_layout.addWidget(self.btn_back_login,alignment=Qt.AlignCenter)

        # Aggiungi il layout dei pulsanti al layout principale
        layout.addLayout(button_layout)

        # Spacer sotto per centrare verticalmente
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Imposta il layout alla pagina 'gestione'
        self.stack.addWidget(self.gestione)

    def init_registra(self):
        self.page_registra = QWidget()
        layout = QVBoxLayout()

        # Mostra un messaggio che l'ID verrà generato automaticamente
        self.label_info = QLabel("Nota: L'ID verrà generato automaticamente.")
        self.label_info.setFont(QFont("Arial", 10))
        layout.addWidget(self.label_info)

        self.input_password_registra = QLineEdit()
        self.input_password_registra.setPlaceholderText("Password")
        self.input_password_registra.setStyleSheet(self.input_style())
        layout.addWidget(self.input_password_registra)


        self.btn_conferma_registra = QPushButton("Conferma")
        self.btn_conferma_registra.setStyleSheet(self.button_style())
        self.btn_conferma_registra.clicked.connect(self.gestione_registra)
        layout.addWidget(self.btn_conferma_registra)

        self.btn_back_registra = QPushButton("Indietro")
        self.btn_back_registra.setStyleSheet(self.button_style())
        self.btn_back_registra.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_registra)

        self.output_registrazione = QTextEdit()
        self.output_registrazione.setReadOnly(True)
        self.output_registrazione.setStyleSheet("background-color: white; border-radius: 8px; padding: 5px;")
        layout.addWidget(self.output_registrazione)

        self.page_registra.setLayout(layout)
        self.stack.addWidget(self.page_registra)

    def button_style(self):
        return "QPushButton {background-color: #007BFF; color: white; border-radius: 10px; padding: 10px; font-size: 14px;} QPushButton:hover {background-color: #0056b3;}"

    def input_style(self):
        return "QLineEdit {border: 2px solid #ccc; border-radius: 10px; padding: 5px; font-size: 14px; background-color: white;}"


    def gestione_login(self):

        # Esegui il login utilizzando il metodo login implementato nella classe Login
        user_id = self.input_id.text()
        password = self.input_password.text()
        if self.login.login(user_id,password):
            self.output.append("Login corretto!")
            self.stack.setCurrentWidget(self.gestione)

        else:
            self.output.append("Login non corretto!")

    def gestione_registra(self):
        password = self.input_password_registra.text().strip()

        if not password:
            self.output_registrazione.setText("⚠️ Errore: Inserisci una password valida!")
            return
        user_id, password = self.login.registra_utente(password)
        self.output_registrazione.setText(f"✅ Registrazione completata!\n\n"
                                          f"🔑 Password: {password}\n"
                                          f"🆔 ID Utente: {user_id}")
        QTimer.singleShot(4000, lambda: self.stack.setCurrentWidget(self.gestione))







