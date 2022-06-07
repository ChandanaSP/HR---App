import frappe
def create_child_employee(doc,action):
    company_doc=frappe.db.get_value('Company',doc.company,"compliance_and_audit")
    child_company=frappe.db.get_value('Company',doc.company,"ts_company_name")
    if(company_doc==1):
        if(doc.enable_esi ==1 or doc.enable_pf ==1):
            emp_doc=frappe.new_doc('Employee')
            emp_doc.update({
                'company':child_company,
                'first_name':doc.first_name,
                'gender':doc.gender,
                'date_of_birth':doc.date_of_birth,
                'date_of_joining':doc.date_of_joining
            })
            emp_doc.save()
            frappe.db.commit()