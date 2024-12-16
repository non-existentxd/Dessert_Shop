from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

def generate_receipt(order_items, subtotal, tax, total, total_items):
    try:

        pdf_path = "receipt.pdf"
        pdf = SimpleDocTemplate(pdf_path, pagesize=A4)


        styles = getSampleStyleSheet()
        title_style = styles["Heading1"]
        title_style.alignment = 1


        title = Paragraph("Dessert Shop Receipt", title_style)
        spacer = Spacer(1, 20) 

        data = [["Name", "Item Cost", "Tax"]]
        for item in order_items:
            if not all(key in item for key in ("Name", "Item Cost", "Tax")):
                raise ValueError("Each item must have 'Name', 'Item Cost', and 'Tax' keys.")
            data.append([item["Name"], f"${item['Item Cost']:.2f}", f"${item['Tax']:.2f}"])


        data.append(["Order Subtotals", f"${subtotal:.2f}", f"${tax:.2f}"])
        data.append(["Order Total", "", f"${total:.2f}"])
        data.append(["Total Items in the Order", "", str(total_items)])

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

        pdf.build([title, spacer, table])
        print(f"Receipt successfully generated at: {pdf_path}")

    except Exception as e:
        print(f"Error generating receipt: {e}")


#i wanna see if this is actually working...

