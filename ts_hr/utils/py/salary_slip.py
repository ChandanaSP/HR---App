
import frappe
import json
from erpnext.payroll.doctype.salary_slip.salary_slip import SalarySlip

@frappe.whitelist()
def salary_slip_based_on_shift(doc,event):
    emp_struct=frappe.db.get_value("Salary Structure", doc.salary_structure, "salary_slip_based_on_shift")
    emp_shift_amount=frappe.db.get_value("Salary Structure", doc.salary_structure, "shift_rate")
    if emp_struct==1:
        shift = frappe.get_all(
            "Attendance",
            fields=["employee",'status'],
            filters=[
                ["attendance_date", ">=", doc.start_date],
                ["attendance_date", "<=", doc.end_date],
                ["employee", "=", doc.employee],
                ["docstatus", "!=", 2],
            ],
        )

        shift_count=0
        for data in shift:
            if(data['status']=='Half Day'):
                shift_count+=.5

            if(data['status']=='One Half Day'):
                shift_count+=1.5  

            elif(data['status']=='Present'):
                shift_count+=1

            elif(data['status']=='Quarter Day'):
                shift_count+=.25

            elif(data['status']=='One Quarter Day'):
                shift_count+=1.25

            elif(data['status']=='Three Quarter Day'):
                shift_count+=.75

    doc.total_shift_worked=shift_count
    doc.set('earnings', [])
    doc.append("earnings", {"salary_component": 'Basic', "amount": shift_count*emp_shift_amount})
    gross_pay=0
    for data in doc.earnings:
        gross_pay+=data.amount
    
    doc.gross_pay=gross_pay
    doc.net_pay=doc.gross_pay-doc.total_deduction
    doc.rounded_total=round(doc.net_pay)    

    #Calculation of year to date
    SalarySlip.compute_year_to_date(doc)
    
    #Calculation of Month to date
    SalarySlip.compute_month_to_date(doc)
    SalarySlip.compute_component_wise_year_to_date(doc)
    SalarySlip.set_net_total_in_words(doc)