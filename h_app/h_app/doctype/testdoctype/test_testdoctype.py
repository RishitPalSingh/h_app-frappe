# # Copyright (c) 2024, Rishit and Contributors
# # See license.txt

# import frappe
# from frappe.tests.utils import FrappeTestCase


# class TestTestDoctype(FrappeTestCase):
# 	def setUP(self):
# 		self.doc=frappe.get_doc({
# 			"doctype":"TestDoctype",
# 			"field_1":55,
# 			"field_2":"Ak47"
# 		}).insert()
# 		frappe.db.commit()
	
# 	def tearDown(self) -> None:
# 		if self.doc.name:
# 			doc3=frappe.get_doc('TestDoctype',self.doc.name)
# 			doc3.delete()
# 			frappe.db.commit()
	
# 	def test_check_field(self):
# 		doc2=frappe.get_doc('TestDoctype',self.doc.name)
# 		self.assertEqual(55,int(doc2.field_1))
		
# 	def test_update_field(self):
# 		doc2=frappe.get_doc('TestDoctype',self.doc.name)
# 		doc2.update({
# 			"field_1":1
# 		})
# 		doc2.save()
# 		frappe.db.commit()
# 		self.assertNotEqual(55,int(doc2.field_1))
	
# Copyright (c) 2024, Rishit and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestTestDoctype(FrappeTestCase):
    def setUp(self):
        # Create a document before each test
        self.doc = frappe.get_doc({
            "doctype": "TestDoctype",
            "field_1": 55,
            "field_2": "Ak47"
        }).insert()
        frappe.db.commit()
    
    def tearDown(self):
        # Delete the document after each test if it exists
        if hasattr(self, 'doc') and self.doc.name:
            doc = frappe.get_doc('TestDoctype', self.doc.name)
            doc.delete()
            frappe.db.commit()
    
    def test_check_field(self):
        # Verify the initial value of field_1
        doc = frappe.get_doc('TestDoctype', self.doc.name)
        self.assertEqual(int(doc.field_1), 55)
        
    def test_update_field(self):
        # Update the value of field_1 and verify the change
        doc = frappe.get_doc('TestDoctype', self.doc.name)
        doc.field_1 = 1
        doc.save()  # Use save() method instead of update() for updating document
        frappe.db.commit()
        
        # Re-fetch the document to verify the update
        doc = frappe.get_doc('TestDoctype', self.doc.name)
        self.assertEqual(int(doc.field_1), 1)



