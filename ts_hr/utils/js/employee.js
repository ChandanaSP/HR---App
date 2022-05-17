frappe.ui.form.on('Employee',{
    validate:function(frm){
        frappe.call({
            method:"ts_hr.utils.py.employee.create_child_employee",
            args:{"doc":frm.doc}
        })
    }
});