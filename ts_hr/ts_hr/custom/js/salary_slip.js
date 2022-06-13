
frappe.ui.form.on("Salary Slip", {
	employee: function(frm) {
        // console.log(frm.doc.salary_structure)
        frappe.db.get_doc('Salary Structure',frm.doc.salary_structure).then(doc => {
            if(doc.salary_slip_based_on_shift==1){
                frappe.call({
                    method: 'ts_hr.ts_hr.custom.js.py.salary_slip.salary_slip_based_on_shift',
                    args: {
                        doc:frm.doc
                    },
                    callback: function (r) {
                        console.log(r.message)
                        if (r.message) {
                            cur_frm.set_value('payment_days', r.message);
                        }
                    }
                });
            }
            refresh_field('payment_days')
        });

        
            
    }
})