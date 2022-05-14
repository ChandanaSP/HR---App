frappe.ui.form.on('Employee',{
    refresh:function(frm){
        if(!frm.is_dirty()){
        frm.add_custom_button(('Salary structure '), function() {
            var doc = frappe.model.get_new_doc('Salary Structure ');
            frappe.set_route('Form', 'Salary Structure', doc.name);
        }).addClass("btn-danger").css({'color':'black','background-color': 'orange','font-weight': 'bold'}); ;
        frm.add_custom_button(('Salary Structure Assignment'), function() {
            var doc = frappe.model.get_new_doc('Salary Structure Assignment');
            frappe.set_route('Form', 'Salary Structure Assignment', doc.name);
        }).addClass("btn-danger").css({'color':'white','background-color': 'red','font-weight': 'bold'});
    }}
})