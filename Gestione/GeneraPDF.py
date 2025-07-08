from fpdf import FPDF
import os


class GestorePDF:
    def __init__(self, output_dir="Dati/PDF"):
        """
        Inizializza il gestore PDF creando la cartella di output se non esiste.
        """
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def genera_pdf(self, documento):
        """
        Genera e salva un PDF per il documento fornito.

        Il file PDF verrà salvato con il nome:
        "{nome_cliente}_{tipo_documento}_{id_documento}.pdf"
        """
        # Crea il nome del file sostituendo gli spazi con underscore
        file_name = f"{documento.cliente.nome}_{documento.tipo_documento}_{documento.id_documento}.pdf"
        file_name = file_name.replace(" ", "_")
        file_path = os.path.join(self.output_dir, file_name)

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Header
        pdf.set_font("Arial", style='B', size=16)
        pdf.cell(0, 10, f"{documento.tipo_documento.upper()}", ln=True, align='C')
        pdf.ln(10)

        # Informazioni Cliente
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(40, 10, "Cliente:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, documento.cliente.nome, ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(40, 10, "Codice Cliente:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, documento.cliente.codice, ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(40, 10, "Indirizzo:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, documento.cliente.indirizzo, ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(40, 10, "Telefono:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, str(documento.cliente.telefono), ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(40, 10, "Email:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, documento.cliente.email, ln=True)
        pdf.ln(10)

        # Informazioni Dipendente e Data
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(40, 10, "Dipendente:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, documento.dipendente.nome, ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(40, 10, "Data:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, documento.data.strftime("%d-%m-%Y"), ln=True)
        pdf.ln(10)

        # Dettagli Prodotto
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(30, 10, "Cod. Prod.:", border=1)
        pdf.cell(50, 10, "Prodotto", border=1)
        pdf.cell(30, 10, "Marca", border=1)
        pdf.cell(20, 10, "Q.ta", border=1)
        pdf.cell(30, 10, "Prezzo cad.1", border=1)
        pdf.cell(30, 10, "Totale ivato", border=1, ln=True)

        pdf.set_font("Arial", size=12)
        pdf.cell(30, 10, documento.prodotto.codice, border=1)
        pdf.cell(50, 10, documento.prodotto.nome, border=1)
        pdf.cell(30, 10, documento.prodotto.marca, border=1)
        pdf.cell(20, 10, str(documento.quantita), border=1)
        pdf.cell(30, 10, f"{documento.prodotto.prezzo:.2f}", border=1)
        pdf.cell(30, 10, f"{((documento.prodotto.prezzo*1.22)*documento.quantita):.2f}", border=1, ln=True)
        pdf.ln(10)

        # Footer
        pdf.set_font("Arial", style='I', size=10)
        pdf.cell(0, 10, "Grazie per aver scelto il nostro negozio!", ln=True, align='C')

        pdf.output(file_path)
        print(f"PDF generato e salvato in: {file_path}")

