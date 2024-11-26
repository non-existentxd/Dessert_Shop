from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

def generate_receipt(order_items, subtotal, tax, total, total_items):
    pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.alignment = 1  


    title = Paragraph("Dessert Shop Receipt", title_style)


    data = [["Name", "Item Cost", "Tax"]]
    for item in order_items:
        data.append(f"{item["Name"]}, ${item['Cost']}, ${item['Tax']}")


    data.append(f"Order Subtotals, ${subtotal}, ${tax}")
    data.append(f"Order Total" "${total}")
    data.append(f"Total Items in the Order {str(total_items)}")


    table_style = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )


    table = Table(data, style=table_style)


    pdf.build([title, table])