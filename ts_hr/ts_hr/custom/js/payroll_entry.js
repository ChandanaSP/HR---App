// frappe.ui.form.on('Payroll Entry',{
//     refresh:function(frm){
//         if (!frm.is_dirty()) {
//         frm.add_custom_button(('Next'), function() {
//             var doc = frappe.model.get_new_doc('Salary Slip');
//             frappe.set_route('Form', 'Salary', doc.name);
//         });
//     }}
// })