from fpdf import FPDF
from datetime import datetime

class MedicalReportPDF(FPDF):
    def header(self):
        self.set_y(10)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Medical Report', align='C', ln=True)
        self.ln(5)

    def add_patient_info_table(self, details):
        self.set_font('Arial', '', 10)

        # Calculate widths to match the image
        w1 = 45  # Name
        w2 = 45  # Age
        w3 = 45  # Sex
        w4 = 30  # Bed
        w5 = 30  # UHID

        # First row
        self.cell(w1, 6, f"Name: {details['name']}", border=1)
        self.cell(w2, 6, f"Age: {details['age']}", border=1)
        self.cell(w3, 6, f"Sex: {details['sex']}", border=1)
        self.cell(w4, 6, f"Bed: {details['bed']}", border=1)
        self.cell(w5, 6, f"UHID: {details['uhid']}", border=1, ln=True)

        # DIAGNOSIS row (two cells)
        diag_label_width = 45
        diag_content_width = w1 + w2 + w3 + w4 + w5 - diag_label_width
        self.cell(diag_label_width, 6, "DIAGNOSIS:", border=1)
        self.cell(diag_content_width, 6, f"{details['diagnosis']}", border=1, ln=True)

        # Consultants row (two cells of equal width)
        total_width = w1 + w2 + w3 + w4 + w5
        half_width = total_width / 2
        self.cell(half_width, 6, f"Consultants: {details['consultants']}", border=1)
        self.cell(half_width, 6, f"JRs: {details['jr']}", border=1, ln=True)
        self.ln(4)

    def add_section(self, title, content, is_bold_title=True):
        if is_bold_title:
            self.set_font('Arial', 'B', 10)
        else:
            self.set_font('Arial', '', 10)

        self.cell(120, 6, title, ln=True)

        self.set_font('Arial', '', 10)
        for line in content:
            # Ensure we don't exceed the page width
            self.multi_cell(120, 6, line)
        self.ln(1)

    def add_side_table(self, table_data):
        start_x = 140  # Moved further right
        start_y = 45

        current_y = self.get_y()

        # Add date header
        self.set_xy(start_x, start_y)
        self.set_font('Arial', 'B', 10)

        self.cell(25, 6, "Date", border=1, align='C')
        self.cell(30, 6, f"{datetime.now().strftime('%d/%m/%Y')}", border=1, align='C', ln=True)

        # Add parameter header
        #self.set_x(start_x)
        #self.cell(25, 6, "Parameter", border=1, align='C')
        #self.cell(30, 6, "Value", border=1, align='C', ln=True)

        # Add table rows
        for key, value in table_data['rows'].items():
            self.set_x(start_x)
            self.cell(25, 6, key, border=1, align='C')
            self.cell(30, 6, value, border=1, align='C', ln=True)

        self.set_xy(10, current_y)


def generate_pdf(fields_data):
    # Create PDF instance with adjusted margins
    pdf = MedicalReportPDF()
    pdf.set_margins(10, 10, 10)
    pdf.set_auto_page_break(True, margin=15)
    pdf.add_page()

    Name =fields_data["Name"]
    Age =fields_data["Age"]
    Sex =fields_data["Sex"]
    Bed =fields_data["Bed"]
    UHID =fields_data["UHID"]
    Diagnosis =fields_data["Diagnosis"]
    Consultants =fields_data["Consultants"]
    Junior_Residents =fields_data["Junior Residents"]
    Feeds =fields_data["Feeds"]
    Ionotropes =fields_data["Ionotropes"]
    Antimicrobials =fields_data["Antimicrobials"]
    Miscellaneous =fields_data["Miscellaneous"]
    Nursing_and_Supportive_Care =fields_data["Nursing and Supportive Care"]

    print(type(fields_data))

    # Add content (same as before)
    pdf.add_patient_info_table({
        'name': f'{Name}',
        'age': f'{Age}',
        'sex': f'{Sex}',
        'bed': f'{Bed}',
        'uhid': f'{UHID}',
        'diagnosis':f'{Diagnosis}',
        'consultants':f'{Consultants}',
        'jr':f'{Junior_Residents}'
    })

    pdf.add_side_table({
        'rows': {
            f'Weight': f'{fields_data["Weight_Values"]} {fields_data["Weight_Units"]}',
            f'TFR': f'{fields_data["TFR_Values"]} {fields_data["TFR_Units"]}',
            f'TFV': f'{fields_data["TFV_Values"]} {fields_data["TFV_Units"]}',
            f'IVF': f'{fields_data["IVF_Values"]} {fields_data["IVF_Units"]}',
            f'IVM': f'{fields_data["IVM_Values"]} {fields_data["IVM_Units"]}',
            f'Glucose': f'{fields_data["Glucose_Values"]} {fields_data["Glucose_Units"]}',
            f'GIR': f'{fields_data["GIR_Values"]} {fields_data["GIR_Units"]}',
            f'Feeds': f'{fields_data["Feeds_Values"]} {fields_data["Feeds_Units"]}',
            f'K': f'{fields_data["K_Values"]} {fields_data["K_Units"]}',
            f'Na': f'{fields_data["Na_Values"]} {fields_data["Na_Units"]}',
        }
    })

    # Add sections with proper spacing
    pdf.add_section("Feeds:", [f'{Feeds}'])

    pdf.add_section("Ionotropes:", [
        f'{Ionotropes}'
    ])

    #pdf.add_section("IVF:", [
    #    "Inj IVF DNS (6ml KCl: 100 ml IVF) @ 12ml per hour (290 ml)"
    #])

    pdf.add_section("Antimicrobials(435 ml):", [
        f'{Antimicrobials}'
    ])

    pdf.add_section("Miscellaneous: (694.4 ml):", [
        f'{Miscellaneous}'
    ])

    pdf.add_section("Nursing and supportive care:", [
        f'{Nursing_and_Supportive_Care}'
    ])


    import time
    import os

    # Get the current time in seconds since the epoch
    current_time_seconds = time.time()

    # Convert to milliseconds
    current_time_milliseconds = int(current_time_seconds * 1000)


    name_of_pdf = f"{current_time_milliseconds}.pdf"

    pdf.output(name_of_pdf)



    os.startfile(name_of_pdf)