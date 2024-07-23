
# import cups
# import frappe
# from frappe import _
# from frappe.utils.pdf import get_pdf
# import os
# # import os

# # Set the environment variable
# # os.environ['XDG_RUNTIME_DIR'] = '/tmp/runtime-erp'

# # Then call your function


# @frappe.whitelist(allow_guest=True)
# def send_to_printer(doctype, name, format=None, doc=None, no_letterhead=0, language=None, letterhead=None):
#     os.environ['XDG_RUNTIME_DIR'] = '/tmp/runtime-erp'
#     print("Send to printer function called")

#     doc = doc or frappe.get_doc(doctype, name)
#     if not frappe.has_permission(doc, 'read'):
#         frappe.throw(_("Not permitted"), frappe.PermissionError)

#     html = frappe.get_print(doctype, name, format, doc=doc, no_letterhead=no_letterhead)
#     print(html,"hjhhhhhhhhhhhhhhhh")
#     # pdf_file = get_pdf(html, options={'--no-stop-slow-scripts': '', '--enable-local-file-access': ''})

#     pdf_file = get_pdf(html)
#     pdf_path = "/tmp/{}.pdf".format(name.replace(" ", "-").replace("/", "-"))
#     with open(pdf_path, "wb") as f:
#         f.write(pdf_file)

#     try:
#         conn = cups.Connection()
#         printers = conn.getPrinters()
#         printer_name = 'POS-80-Series'
#         if printer_name not in printers:
#             frappe.throw(_("Printer not found"), frappe.FileNotFoundError)

#         conn.printFile(printer_name, pdf_path, "Print Job", {})
#         print("Print job sent successfully")
#     except Exception as e:
#         print("Error sending print job:", e)
#         frappe.throw(_("Error sending print job"))

#     os.remove(pdf_path)
#     return _("Print job sent successfully")

import cups
import frappe
from frappe import _
from frappe.utils.pdf import get_pdf
import os
import subprocess
import socket

def print_pdf(file_path, printer_name=None):
    command = ['lpr']
    if printer_name:
        command += ['-P', printer_name]
    command.append(file_path)

    try:
        subprocess.run(command, check=True)
        print(f"Printing {file_path} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to print the file: {e}")

# # Example usage
# pdf_file_path = '/tmp/PUR-ORD-2024-00001.pdf'
# printer_name = 'your_printer_name'  # Replace with your actual printer name if needed
# print_pdf(pdf_file_path, printer_name)



@frappe.whitelist(allow_guest=True)
def send_to_printer(doctype, name, format=None, doc=None, no_letterhead=0, language=None, letterhead=None):
    print("Send to printer function called")

    # Set the environment variable
    os.environ['XDG_RUNTIME_DIR'] = '/tmp/runtime-erp'

    # Use simplified HTML for testing
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Document</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                color: #333;
            }
            .header {
                background-color: #f5f5f5;
                padding: 10px;
                text-align: center;
            }
            .content {
                padding: 20px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Test Document</h1>
        </div>
        <div class="content">
            <p>This is a test document.</p>
        </div>
    </body>
    </html>
    """
    print("HTML generated for document")

    try:
        # Generate PDF without unsupported options
        pdf_file = get_pdf(html)
        pdf_path = "/tmp/{}.pdf".format(name.replace(" ", "-").replace("/", "-"))
        print(pdf_path)
        with open(pdf_path, "wb") as f:
            f.write(pdf_file)

        # Verify that the file was created
        if not os.path.exists(pdf_path):
            raise FileNotFoundError("Failed to create PDF file")

        print(f"PDF file created at: {pdf_path}")

        conn = cups.Connection()
        # printers = conn.getPrinters()
        PRINTER_IP = "192.168.1.23"
        PRINTER_PORT = 9100
        printer_name = 'POS-80-Series'
        conn.printFile(printer_name, pdf_path, "Print Job", {})

        # # if printer_name not in printers:
        # #     raise FileNotFoundError("Printer not found")
# Create a socket connection to the printer
        # printer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # printer_socket.connect((PRINTER_IP, PRINTER_PORT))

        # Send the PDF file to the printer
        # printer_socket.sendall(pdf_file)
        # printer_socket.close()
        # conn.printFile(printer_name, pdf_path, "Print Job", {})
       
        # print_pdf(pdf_path,printer_name)
        print("Print job sent successfully")

    except FileNotFoundError as e:
        print("Error sending print job:", e)
        frappe.throw(_("Printer not found"))
    except cups.IPPError as e:
        print("CUPS IPP Error:", e)
        frappe.throw(_("Error sending print job: {}").format(e))
    except Exception as e:
        print("Error sending print job:", e)
        frappe.throw(_("Error sending print job"))

    finally:
        # Clean up the temporary file if it exists
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
            print(f"Temporary PDF file {pdf_path} removed")
        else:
            print(f"Temporary PDF file {pdf_path} does not exist")

    return _("Print job sent successfully")

