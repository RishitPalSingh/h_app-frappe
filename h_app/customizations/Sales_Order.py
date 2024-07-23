import frappe
import frappe.utils

def AnniversaryValidate(doc,method):
#    frappe.throw("LLLLLLLLLLLLLLLLL")
   frappe.msgprint(doc.contact_email)