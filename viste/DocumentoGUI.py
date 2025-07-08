from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, \
    QStackedWidget, QCheckBox, QDesktopWidget, QTableWidgetItem, QTableWidget, QSpacerItem, QSizePolicy, QInputDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Controller.ControllerPDF import ControllerPDF
from Controller.ControllerDocumenti import ControllerDocumenti



class DocumentiGUI(QWidget):
    def __init__(self, main_gui):
        super().__init__()
        self.main_gui = main_gui
        self.controller_pdf = ControllerPDF()
        self.controller = ControllerDocumenti()
        # Creiamo un QTableWidget per visualizzare i documenti in stile tabellare
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID", "Data", "Tipo", "Dipendente", "Cod. Cliente", "Cliente", "Indirizzo", "Telefono", "Email", "Cod. Prodotto", "Prodotto", "Quantità", "Marca", "prezzo", "Prezzo ivato",
        ])
        self.init_ui()
        self.center()


    def init_ui(self):
        self.setWindowTitle("Gestione Documenti")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f4f4f4;")
        self.stack = QStackedWidget()
        self.layout_principale = QVBoxLayout(self)
        self.layout_principale.addWidget(self.stack)

        self.init_home()
        self.init_aggiungi()
        self.init_modifica()
        self.init_rimuovi()
        self.init_visualizza()
        self.init_doc_clienti()
        self.init_pdf()

        self.setLayout(self.layout_principale)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_home(self):
        self.home = QWidget()
        layout = QVBoxLayout(self.home)

        self.label_titolo = QLabel("GESTIONE DOCUMENTI")
        self.label_titolo.setFont(QFont("Arial", 16, QFont.Bold))
        self.label_titolo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_titolo)

        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        button_size = (200, 40)

        self.btn_aggiungi = QPushButton("Aggiungi Documento")
        self.btn_aggiungi.setFixedSize(*button_size)
        self.btn_aggiungi.setStyleSheet(self.button_style())
        self.btn_aggiungi.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_aggiungi))
        layout.addWidget(self.btn_aggiungi, alignment=Qt.AlignCenter)

        self.btn_modifica = QPushButton("Modifica Documento")
        self.btn_modifica.setFixedSize(*button_size)
        self.btn_modifica.setStyleSheet(self.button_style())
        self.btn_modifica.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_modifica))
        layout.addWidget(self.btn_modifica, alignment=Qt.AlignCenter)

        self.btn_rimuovi = QPushButton("Rimuovi Documento")
        self.btn_rimuovi.setFixedSize(*button_size)
        self.btn_rimuovi.setStyleSheet(self.button_style())
        self.btn_rimuovi.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_rimuovi))
        layout.addWidget(self.btn_rimuovi, alignment=Qt.AlignCenter)

        self.btn_visualizza = QPushButton("Visualizza Documenti")
        self.btn_visualizza.setFixedSize(*button_size)
        self.btn_visualizza.setStyleSheet(self.button_style())
        self.btn_visualizza.clicked.connect(self.visualizza_doc)
        layout.addWidget(self.btn_visualizza, alignment=Qt.AlignCenter)

        self.btn_doc_clienti = QPushButton("Visualizza Doc. Clienti")
        self.btn_doc_clienti.setFixedSize(*button_size)
        self.btn_doc_clienti.setStyleSheet(self.button_style())
        self.btn_doc_clienti.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_doc_clienti))
        layout.addWidget(self.btn_doc_clienti, alignment=Qt.AlignCenter)

        self.btn_pdf = QPushButton("Genera PDF")
        self.btn_pdf.setFixedSize(*button_size)
        self.btn_pdf.setStyleSheet(self.button_style())
        self.btn_pdf.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_pdf))
        layout.addWidget(self.btn_pdf, alignment=Qt.AlignCenter)

        self.btn_back = QPushButton("Torna alla Gestione")
        self.btn_back.setFixedSize(*button_size)
        self.btn_back.setStyleSheet(self.button_style())
        self.btn_back.clicked.connect(self.back_to_gestione)
        layout.addWidget(self.btn_back, alignment=Qt.AlignCenter)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: white; border-radius: 8px; padding: 5px;")
        layout.addWidget(self.output)

        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.stack.addWidget(self.home)

    def init_aggiungi(self):
        self.page_aggiungi = QWidget()
        layout = QVBoxLayout()

        self.input_data = QLineEdit()
        self.input_data.setPlaceholderText("Data (dd-mm-yyyy)")
        self.input_data.setStyleSheet(self.input_style())
        layout.addWidget(self.input_data)

        self.input_dipendente = QLineEdit()
        self.input_dipendente.setPlaceholderText("Nome Dipendente")
        self.input_dipendente.setStyleSheet(self.input_style())
        layout.addWidget(self.input_dipendente)

        self.input_cliente = QLineEdit()
        self.input_cliente.setPlaceholderText("Nome Cliente")
        self.input_cliente.setStyleSheet(self.input_style())
        layout.addWidget(self.input_cliente)

        self.input_prodotto = QLineEdit()
        self.input_prodotto.setPlaceholderText("Nome Prodotto")
        self.input_prodotto.setStyleSheet(self.input_style())
        layout.addWidget(self.input_prodotto)

        self.input_quantita = QLineEdit()
        self.input_quantita.setPlaceholderText("Quantità")
        self.input_quantita.setStyleSheet(self.input_style())
        layout.addWidget(self.input_quantita)

        self.btn_conferma_aggiungi = QPushButton("Conferma")
        self.btn_conferma_aggiungi.setStyleSheet(self.button_style())
        self.btn_conferma_aggiungi.clicked.connect(self.aggiungi_doc)
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
        self.input_codice_mod.setPlaceholderText("ID Documento")
        self.input_codice_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice_mod)

        self.input_data_mod = QLineEdit()
        self.input_data_mod.setPlaceholderText("Nuova Data (dd-mm-yyyy)")
        self.input_data_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_data_mod)

        self.input_dipendente_mod = QLineEdit()
        self.input_dipendente_mod.setPlaceholderText("Nuovo Nome Dipendente")
        self.input_dipendente_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_dipendente_mod)

        self.input_cliente_mod = QLineEdit()
        self.input_cliente_mod.setPlaceholderText("Nuovo Nome Cliente")
        self.input_cliente_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_cliente_mod)

        self.input_prodotto_mod = QLineEdit()
        self.input_prodotto_mod.setPlaceholderText("Nuovo Nome Prodotto")
        self.input_prodotto_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_prodotto_mod)

        self.input_quantita_mod = QLineEdit()
        self.input_quantita_mod.setPlaceholderText("Nuova Quantità")
        self.input_quantita_mod.setStyleSheet(self.input_style())
        layout.addWidget(self.input_quantita_mod)

        self.btn_conferma_modifica = QPushButton("Conferma Modifica")
        self.btn_conferma_modifica.setStyleSheet(self.button_style())
        self.btn_conferma_modifica.clicked.connect(self.modifica_doc)
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
        self.input_codice_rim.setPlaceholderText("ID Documento")
        self.input_codice_rim.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice_rim)

        self.btn_conferma_rimuovi = QPushButton("Conferma Rimuovi")
        self.btn_conferma_rimuovi.setStyleSheet(self.button_style())
        self.btn_conferma_rimuovi.clicked.connect(self.rimuovi_doc)
        layout.addWidget(self.btn_conferma_rimuovi)

        self.btn_back_rim = QPushButton("Indietro")
        self.btn_back_rim.setStyleSheet(self.button_style())
        self.btn_back_rim.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_rim)

        self.page_rimuovi.setLayout(layout)
        self.stack.addWidget(self.page_rimuovi)

    def init_visualizza(self):
        self.page_visualizza = QWidget()
        layout = QVBoxLayout()

        self.input_codice_vis = QLineEdit()
        self.input_codice_vis.setPlaceholderText("ID Documento (lascia vuoto per tutti)")
        self.input_codice_vis.setStyleSheet(self.input_style())
        layout.addWidget(self.input_codice_vis)

        self.btn_conferma_visualizza = QPushButton("Conferma Visualizza")
        self.btn_conferma_visualizza.setStyleSheet(self.button_style())
        self.btn_conferma_visualizza.clicked.connect(self.visualizza_doc)
        layout.addWidget(self.btn_conferma_visualizza)

        # Inseriamo il tableWidget per visualizzare i documenti in forma tabellare
        layout.addWidget(self.tableWidget)

        self.btn_back_vis = QPushButton("Indietro")
        self.btn_back_vis.setStyleSheet(self.button_style())
        self.btn_back_vis.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_vis)



        self.page_visualizza.setLayout(layout)
        self.stack.addWidget(self.page_visualizza)

    def init_doc_clienti(self):
        self.page_doc_clienti = QWidget()
        layout = QVBoxLayout()

        self.input_nome_cliente = QLineEdit()
        self.input_nome_cliente.setPlaceholderText("Nome Cliente")
        self.input_nome_cliente.setStyleSheet(self.input_style())
        layout.addWidget(self.input_nome_cliente)

        self.btn_conferma_doc_cli = QPushButton("Conferma Visualizza")
        self.btn_conferma_doc_cli.setStyleSheet(self.button_style())
        self.btn_conferma_doc_cli.clicked.connect(self.visualizza_doc_cli)
        layout.addWidget(self.btn_conferma_doc_cli)

        # Creazione di un QTableWidget dedicato per la visualizzazione dei documenti per cliente
        self.tableWidget_doccli = QTableWidget(self)
        self.tableWidget_doccli.setRowCount(0)
        self.tableWidget_doccli.setColumnCount(15)
        self.tableWidget_doccli.setHorizontalHeaderLabels([
            "ID", "Data", "Tipo", "Dipendente", "Cod. Cliente", "Cliente", "Indirizzo", "Telefono", "Email",
            "Cod. Prodotto", "Prodotto", "Quantità", "Marca", "prezzo", "Prezzo ivato",
        ])
        layout.addWidget(self.tableWidget_doccli)

        self.btn_back_doc_cli = QPushButton("Indietro")
        self.btn_back_doc_cli.setStyleSheet(self.button_style())
        self.btn_back_doc_cli.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_doc_cli)


        self.page_doc_clienti.setLayout(layout)
        self.stack.addWidget(self.page_doc_clienti)

    def init_pdf(self):
        self.page_pdf = QWidget()
        layout = QVBoxLayout()

        self.input_cliente_pdf = QLineEdit()
        self.input_cliente_pdf.setPlaceholderText("Nome Cliente")
        self.input_cliente_pdf.setStyleSheet(self.input_style())
        layout.addWidget(self.input_cliente_pdf)

        self.input_tipo_pdf = QLineEdit()
        self.input_tipo_pdf.setPlaceholderText("Tipo Documento")
        self.input_tipo_pdf.setStyleSheet(self.input_style())
        layout.addWidget(self.input_tipo_pdf)

        self.btn_conferma_pdf = QPushButton("Conferma Generazione PDF")
        self.btn_conferma_pdf.setStyleSheet(self.button_style())
        self.btn_conferma_pdf.clicked.connect(self.pdf)
        layout.addWidget(self.btn_conferma_pdf)

        self.btn_back_pdf = QPushButton("Indietro")
        self.btn_back_pdf.setStyleSheet(self.button_style())
        self.btn_back_pdf.clicked.connect(lambda: self.stack.setCurrentWidget(self.home))
        layout.addWidget(self.btn_back_pdf)

        self.page_pdf.setLayout(layout)
        self.stack.addWidget(self.page_pdf)

    def aggiungi_doc(self):
        data = self.input_data.text().strip()
        nome_dipendente = self.input_dipendente.text().strip()
        nome_cliente = self.input_cliente.text().strip()
        nome_prodotto = self.input_prodotto.text().strip()
        quantita = self.input_quantita.text().strip()

        if data and nome_dipendente and nome_cliente and nome_prodotto and quantita:
            try:
                quantita = int(quantita)
                documento = self.controller.aggiungi_documento(data, nome_dipendente, nome_cliente, nome_prodotto,
                                                               quantita)
                if documento:
                    self.output.append(f"✅ Documento aggiunto correttamente!\n{documento}")
                else:
                    self.output.append("⚠️ Errore nella creazione del documento!")
            except ValueError:
                self.output.append("Quantità deve essere numerico e la data deve avere il formato dd-mm-yyyy!")
        else:
            self.output.append("Inserisci tutti i dati!")
        self.stack.setCurrentWidget(self.home)

    def modifica_doc(self):
        id_doc = self.input_codice_mod.text().strip()
        data_mod = self.input_data_mod.text().strip()
        nome_dipendente_mod = self.input_dipendente_mod.text().strip()
        nome_cliente_mod = self.input_cliente_mod.text().strip()
        nome_prodotto_mod = self.input_prodotto_mod.text().strip()
        quantita_mod = self.input_quantita_mod.text().strip()

        if id_doc:
            try:
                if quantita_mod:
                    quantita_mod = int(quantita_mod)
                documento = self.controller.modifica_documento(
                    id_doc,
                    data_mod if data_mod else None,
                    nome_dipendente_mod if nome_dipendente_mod else None,
                    nome_cliente_mod if nome_cliente_mod else None,
                    nome_prodotto_mod if nome_prodotto_mod else None,
                    quantita_mod if quantita_mod else None
                )
                if documento:
                    self.output.append(f"✅ Documento modificato correttamente!\n{documento}")
                else:
                    self.output.append("⚠️ Errore nella modifica del documento!")
            except ValueError:
                self.output.append("Quantità deve essere numerico!")
        else:
            self.output.append("Inserisci l'ID del documento da modificare!")
        self.stack.setCurrentWidget(self.home)

    def rimuovi_doc(self):
        id_doc = self.input_codice_rim.text().strip()
        if id_doc:
            risultato = self.controller.rimuovi_documento(id_doc)
            if risultato:
                self.output.append("✅ Documento rimosso correttamente!")
            else:
                self.output.append("⚠️ Documento non trovato!")
        else:
            self.output.append("Inserisci l'ID del documento da rimuovere!")
        self.stack.setCurrentWidget(self.home)

    def visualizza_doc(self):
        self.output.clear()
        id_doc = self.input_codice_vis.text().strip()
        documenti = self.controller.visualizza_documento(id_doc if id_doc else None)

        # Pulizia della tabella
        self.tableWidget.setRowCount(0)
        # Popoliamo la tabella con i dati dei documenti
        for doc in documenti:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(doc.id_documento))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(doc.data.strftime("%d-%m-%Y")))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(doc.tipo_documento))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(doc.dipendente.nome))
            self.tableWidget.setItem(row_position, 4, QTableWidgetItem(doc.cliente.codice))
            self.tableWidget.setItem(row_position, 5, QTableWidgetItem(doc.cliente.nome))
            self.tableWidget.setItem(row_position, 6, QTableWidgetItem(doc.cliente.indirizzo))
            self.tableWidget.setItem(row_position, 7, QTableWidgetItem(str(doc.cliente.telefono)))
            self.tableWidget.setItem(row_position, 8, QTableWidgetItem(doc.cliente.email))
            self.tableWidget.setItem(row_position, 9, QTableWidgetItem(doc.prodotto.codice))
            self.tableWidget.setItem(row_position, 10, QTableWidgetItem(doc.prodotto.nome))
            self.tableWidget.setItem(row_position, 11, QTableWidgetItem(str(doc.quantita)))
            self.tableWidget.setItem(row_position, 12, QTableWidgetItem(doc.prodotto.marca))
            self.tableWidget.setItem(row_position, 13, QTableWidgetItem(str(doc.prodotto.prezzo)))
            self.tableWidget.setItem(row_position, 14, QTableWidgetItem(str((doc.prodotto.prezzo*1.22)*doc.quantita)))


        self.stack.setCurrentWidget(self.page_visualizza)

    def visualizza_doc_cli(self):
        self.output.clear()
        nome = self.input_nome_cliente.text().strip()
        documenti = self.controller.ricerca_documento(nome)
        self.tableWidget_doccli.setRowCount(0)

        for doc in documenti:
            row_position = self.tableWidget_doccli.rowCount()
            self.tableWidget_doccli.insertRow(row_position)
            self.tableWidget_doccli.setItem(row_position, 0, QTableWidgetItem(doc.id_documento))
            self.tableWidget_doccli.setItem(row_position, 1, QTableWidgetItem(doc.data.strftime("%d-%m-%Y")))
            self.tableWidget_doccli.setItem(row_position, 2, QTableWidgetItem(doc.tipo_documento))
            self.tableWidget_doccli.setItem(row_position, 3, QTableWidgetItem(doc.dipendente.nome))
            self.tableWidget_doccli.setItem(row_position, 4, QTableWidgetItem(doc.cliente.codice))
            self.tableWidget_doccli.setItem(row_position, 5, QTableWidgetItem(doc.cliente.nome))
            self.tableWidget_doccli.setItem(row_position, 6, QTableWidgetItem(doc.cliente.indirizzo))
            self.tableWidget_doccli.setItem(row_position, 7, QTableWidgetItem(str(doc.cliente.telefono)))
            self.tableWidget_doccli.setItem(row_position, 8, QTableWidgetItem(doc.cliente.email))
            self.tableWidget_doccli.setItem(row_position, 9, QTableWidgetItem(doc.prodotto.codice))
            self.tableWidget_doccli.setItem(row_position, 10, QTableWidgetItem(doc.prodotto.nome))
            self.tableWidget_doccli.setItem(row_position, 11, QTableWidgetItem(str(doc.quantita)))
            self.tableWidget_doccli.setItem(row_position, 12, QTableWidgetItem(doc.prodotto.marca))
            self.tableWidget_doccli.setItem(row_position, 13, QTableWidgetItem(str(doc.prodotto.prezzo)))
            self.tableWidget_doccli.setItem(row_position, 14, QTableWidgetItem(str((doc.prodotto.prezzo*1.22)*doc.quantita)))
        self.stack.setCurrentWidget(self.page_doc_clienti)

    def pdf(self):
        self.output.clear()
        nome = self.input_cliente_pdf.text().strip()
        tipo = self.input_tipo_pdf.text().strip()

        # Validazione input
        if not nome or not tipo:
            self.output.append("Inserisci il nome del cliente e il tipo di documento!")
            self.stack.setCurrentWidget(self.home)
            return

        # Ricerca documenti
        documenti = self.controller.ricerca_documento_pdf(nome, tipo)
        if not documenti:
            self.output.append("Nessun documento trovato per questi parametri!")
            self.stack.setCurrentWidget(self.home)
            return

        # Gestione singolo documento se per quel nome ho 1 o più documenti
        if len(documenti) == 1:
            documento = documenti[0]
        else:
            # Gestione selezione multipla
            items = [f"{doc.id_documento} - {doc.data.strftime('%d-%m-%Y')} - {doc.tipo_documento}"
                     for doc in documenti]

            item, ok = QInputDialog.getItem(
                self, "Seleziona Documento", "Scegli il documento:", items, 0, False
            )

            if not ok or not item:
                self.output.append("Nessun documento selezionato!")
                self.stack.setCurrentWidget(self.home)
                return

            id_selected = item.split(" - ")[0]
            documento = next((doc for doc in documenti if doc.id_documento == id_selected), None)

            if not documento:
                self.output.append("Documento non trovato!")
                self.stack.setCurrentWidget(self.home)
                return

        # Generazione PDF
        from Controller.ControllerPDF import GestorePDF
        pdf_manager = GestorePDF()
        pdf_manager.genera_pdf(documento)
        self.output.append(f"PDF generato per il cliente {nome} con documento {documento.id_documento}")
        self.stack.setCurrentWidget(self.home)

    def back_to_gestione(self):
        self.main_gui.stack.setCurrentWidget(self.main_gui.gestione)

    def button_style(self):
        return ("QPushButton {background-color: #007BFF; color: white; border-radius: 10px; "
                "padding: 10px; font-size: 14px;} QPushButton:hover {background-color: #0056b3;}")

    def input_style(self):
        return ("QLineEdit {border: 2px solid #ccc; border-radius: 10px; padding: 5px; "
                "font-size: 14px; background-color: white;}")
