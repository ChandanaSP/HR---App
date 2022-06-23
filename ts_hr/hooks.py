from . import __version__ as app_version

app_name = "ts_hr"
app_title = "Ts Hr"
app_publisher = "Ts Hr"
app_description = "Ts Hr"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ts_hr@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ts_hr/css/ts_hr.css"
# app_include_js = "/assets/ts_hr/js/ts_hr.js"

# include js, css files in header of web template
# web_include_css = "/assets/ts_hr/css/ts_hr.css"
# web_include_js = "/assets/ts_hr/js/ts_hr.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ts_hr/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Employee" : "ts_hr/custom/js/employee.js",
		 "Salary Structure Assignment" : "ts_hr/custom/js/py/salary_structure_assignment.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ts_hr.install.before_install"
# after_install = "ts_hr.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ts_hr.uninstall.before_uninstall"
# after_uninstall = "ts_hr.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ts_hr.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Employee": {
		"after_insert": "ts_hr.utils.py.employee.create_child_employee"
	},
	"Salary Slip":{
		"validate":"ts_hr.utils.py.salary_slip.salary_slip_based_on_shift"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ts_hr.tasks.all"
# 	],
# 	"daily": [
# 		"ts_hr.tasks.daily"
# 	],
# 	"hourly": [
# 		"ts_hr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ts_hr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ts_hr.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ts_hr.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ts_hr.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ts_hr.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
 

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ts_hr.auth.validate"
# ]

