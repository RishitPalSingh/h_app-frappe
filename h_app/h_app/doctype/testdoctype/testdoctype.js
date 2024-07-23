// Copyright (c) 2024, Rishit and contributors
// For license information, please see license.txt

frappe.ui.form.on("TestDoctype", {
	refresh(frm) {
open_add_new_item_dialog(frm);
	},
});
function open_add_new_item_dialog(frm) {
    let d = new frappe.ui.Dialog({
        title: ('Add New Item'),
        fields: [
        
            {
                fieldname: 'item',
                label: ('Item'),
                fieldtype: 'Link',
                options: 'Item',
                reqd: 1,
            },
            {
                fieldname: 'item_name',
                label: ('Item Name'),
                fieldtype: 'Data',
            
            },
            {
                fieldname: 'quantity',
                label: ('Quantity'),
                fieldtype: 'Int',
                reqd: 1}
        
        ],
        primary_action_label: ('Add Item'),
        primary_action(values) {
       
            frm.doc.field_1=values.quantity;
            frm.doc.field_2=values.item_name;
            frm.refresh_field('field_1');
            frm.refresh_field('field_2');

            d.hide();
            
            frm.save();
        }
    });
    d.show();
}
