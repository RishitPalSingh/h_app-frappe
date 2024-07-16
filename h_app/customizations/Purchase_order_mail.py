import frappe
def mailer(doc,method):
    if doc.docstatus==1:
        recipients="rishuone2053@gmail.com"
        subject=f" Purchase Order is Submitted and DocName -{doc.name} "
        message="""
                    Dear supplier,
                    Purchase Order is Submitted
                """
        frappe.sendmail(
            recipients=recipients,
            subject=subject,
            message=message,
            delayed=False
        )



