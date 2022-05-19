frappe.ui.form.on("Employee Bonus Tool",{
	designation:function(frm,cdt,cdn){
		var bonus=locals[cdt][cdn]
		var bonus1=bonus.designation
		frappe.call({
			method:"ts_hr.ts_hr.doctype.employee_bonus_tool.employee_bonus_tool.employee_finder",
			args:{bonus1},
			callback(r){
				frm.clear_table("employee_bonus");
				for(var i=0;i<r.message.length;i++){
					var child = cur_frm.add_child("employee_bonus");
					frappe.model.set_value(child.doctype, child.name, "bonus_amount", r.message[i]["name"])
					frappe.model.set_value(child.doctype, child.name, "employee_name", r.message[i]["employee_name"])
					// frappe.model.set_value(child.doctype, child.name, "designation", bonus1)
					// // if (frm.doc.designation == "Labour Worker"){
					// 	frappe.model.set_value(child.doctype, child.name, "payment_method",'Deduct from Salary')
					// }
				}
				cur_frm.refresh_field("employee_bonus")
			}
		})

	},
	
	on_submit:function(frm,cdt,cdn){
		var bonus=locals[cdt][cdn]
		console.log(bonus.employee_bonus.length)
		for(var i=0;i<bonus.employee_bonus.length;i++){
            console.log("hiiiiiiiiiiiiiiiiii")
			frappe.call({
				method:"ts_hr.ts_hr.doctype.employee_bonus_tool.employee_bonus_tool.create_retention_bonus",
				args:{bonus_amount:bonus.employee_bonus[i].bonus_amount,
					employee:bonus.employee_bonus[i].employee,
					salary_component:bonus.employee_bonus[i].salary_component,
					date:frm.doc.date,
					// date:frm.doc.date,
					// payment_type:bonus.employee_bonus[i].payment_method
                },
			})
		}
	}})