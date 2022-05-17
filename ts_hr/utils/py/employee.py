import frappe
import json
@frappe.whitelist()
def create_child_employee(doc):
    doc=json.loads(doc)
    company_doc=frappe.db.get_value('Company',doc["company"],"compliance_and_audit")
    child_company=frappe.db.get_value('Company',doc["company"],"ts_company_name")
    if(company_doc==1):
        if(doc['enable_esi']==1 or doc['enable_pf']==1):
            emp_doc=frappe.new_doc('Employee')
            emp_doc.update(doc)
            emp_doc.update({'company':child_company})
            emp_doc.save()