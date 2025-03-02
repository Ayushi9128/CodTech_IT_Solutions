import csv
from fpdf import FPDF

def read_data_from_csv(file_name):
    data = []
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            data.append(row)
    return data


def analyze_data(data):
    total = 0
    count = 0
    for row in data:
        try:
            value = float(row[1])  
            total += value
            count += 1
        except ValueError:
            continue  
    average = total / count if count > 0 else 0
    return total, average


def generate_pdf_report(data, total, average, output_pdf):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt="Automated Report", ln=True, align='C')

    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, txt=f"Total Value: {total}", ln=True)
    pdf.cell(200, 10, txt=f"Average Value: {average}", ln=True)

    pdf.ln(10)
    pdf.cell(40, 10, "ID", border=1)
    pdf.cell(80, 10, "Value", border=1)
    pdf.ln()
    
    for row in data:
        pdf.cell(40, 10, row[0], border=1)  
        pdf.cell(80, 10, row[1], border=1)  
        pdf.ln()

    pdf.output(output_pdf)

# Main Function
def main():
    file_name = "Toyota.csv"  
    output_pdf = "reportCodTech.pdf" 

    data = read_data_from_csv(file_name)
    total, average = analyze_data(data)
    generate_pdf_report(data, total, average, output_pdf)
    print(f"Report generated and saved as {output_pdf}")

if __name__ == "__main__":
    main()
