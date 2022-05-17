import frappe

from frappe.model.document import Document

class EmployeeBonusTool(Document):
	pass
@frappe.whitelist()
def employee_finder(bonus1):
	employee_names=[]
	a=frappe.db.get_all("Employee",fields=["employee", "employee_name"])
	for name in a:
		employee_names.append(name)
	return employee_names
@frappe.whitelist()
def create_retention_bonus(employee,bonus_amount,salary_component,date):
	bonus_doc=frappe.new_doc('Retention Bonus')
	bonus_doc.employee = employee
	bonus_doc.bonus_amount = bonus_amount
	bonus_doc.salary_component = salary_component
	bonus_doc.bonus_payment_date=date
	# bonus_doc.exchange_rate = 1.0
	# if payment_type=="Deduct from Salary":
	# 	bonus_doc.repay_unclaimed_amount_from_salary=1
	bonus_doc.insert()
	bonus_doc.save()
	bonus_doc.submit()
	frappe.db.commit()