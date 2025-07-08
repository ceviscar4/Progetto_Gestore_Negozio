from Gestione.GeneraPDF import GestorePDF

class ControllerPDF:
    def __init__(self):
        self.gestorePDF = GestorePDF()

    def genera_pdf(self, documento):
        return self.gestorePDF.genera_pdf(documento)

