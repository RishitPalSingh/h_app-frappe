import frappe
import frappe.utils

def AnniversaryValidate(doc,method):
    if doc.custom_customer_anniversary and doc.custom_customer_anniversary > frappe.utils.today():
        frappe.throw("You Can't Choose Future Date")

def test_code():
    import ipdb;ipdb.set_trace()
    a=1
    b=4
    print(a+b)

def example_customERR():
    try:
        a=1/0
        print(a)
    except Exception as e :
        frappe.log_error("Can't divide by 0")