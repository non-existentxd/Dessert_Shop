from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

def generate_receipt(data, file_name):
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.alignment = 1 
    body_style = styles["BodyText"]


    elements.append(Paragraph("Dessert Shop Receipt", title_style))
    elements.append(Spacer(1, 12)) 

   
    table_data = data 


    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'), 
        ('ALIGN', (0, 0), (0, -1), 'LEFT'), 
        ('GRID', (0, 0), (-1, -1), 1, colors.black), 
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12), 
    ])


    receipt_table = Table(table_data, colWidths=[150, 75, 75, 75, 75, 100]) 
    receipt_table.setStyle(table_style)


    elements.append(receipt_table)


    doc.build(elements)
