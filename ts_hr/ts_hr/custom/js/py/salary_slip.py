
import frappe
import json
@frappe.whitelist()
def salary_slip_based_on_shift(doc):
        doc=json.loads(doc)
        shift = frappe.get_all(
		"Attendance",
		fields=["employee",'status'],
		filters=[
			["attendance_date", ">=", doc['start_date']],
			["attendance_date", "<=", doc['end_date']],
			["employee", "=", doc['employee']],
			["docstatus", "!=", 2],
		],
	)
        shift_count=0
        for data in shift:
            if(data['status']=='Half Day'):
                shift_count+=.5
                
            elif(data['status']=='Present'):
                shift_count+=1

            elif(data['status']=='Quarter Day'):
                shift_count+=.25

            elif(data['status']=='Three Quarter Day'):
                shift_count+=.75
        print(shift_count)
        return shift_count