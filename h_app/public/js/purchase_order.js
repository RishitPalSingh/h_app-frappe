// Add custom buttons to the "Purchase Order" form
frappe.ui.form.on('Purchase Order', {
    refresh(frm) {
        frm.add_custom_button('PRINT SILENTLY TO PRINTER 1', () => {
            send2bridge(frm, "after the print demo", "INVOICE");
        });
        frm.add_custom_button('PRINT SILENT & REMOTELY', () => {send2bridgeRemote(frm, "after the print demo", "INVOICE")})
        // frm.add_custom_button('PRINT SILENTLY TO PRINTER 2', () => {
        //     send2bridge(frm, "Standard", "PRINTER 2");
        // });
    }
});

// Function to handle silent printing
var send2bridge = function (frm, print_format, print_type) {
    console.log(frm, print_format, print_type)
    // Initialize the web socket for the bridge
  
      var printService = new frappe.silent_print.WebSocketPrinter();
    // Call the server-side method to create a PDF
    frappe.call({
        method: 'silent_print.utils.print_format.create_pdf',
        args: {
            doctype: frm.doc.doctype,
            name: frm.doc.name,
            silent_print_format: print_format,
            // no_letterhead: 1,
            // _lang: "es"
        },
        callback: (r) => {
            console.log(r,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
            // Send the PDF to the printer
            printService.submit({
                'type': print_type, // Printer identifier in WHB's configuration
                'url': 'file.pdf',
                'file_content': r.message.pdf_base64
            });
        }
    });
}

var send2bridgeRemote = function (frm, print_format, print_type){
	frappe.call({
		method: 'silent_print.utils.print_format.print_silently1',
		args: {
			doctype: frm.doc.doctype,
			name: frm.doc.name,
			print_format: print_format,
			print_type: print_type
		}
	})
}