app_name = "multibranch"
app_title = "Multibranch"
app_publisher = "Faircode Next Pvt. Ltd."
app_description = "This module is designed for a company with multiple branches that requires staff confidentiality. Each branch will have its own unique series for all transactions, and each transaction will be accounted for in its respective cost center. This setup enables branch-specific reporting across all major reports. "
app_email = "nakul@faircodetech.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "multibranch",
# 		"logo": "/assets/multibranch/logo.png",
# 		"title": "Multibranch",
# 		"route": "/multibranch",
# 		"has_permission": "multibranch.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/multibranch/css/multibranch.css"
# app_include_js = "/assets/multibranch/js/multibranch.js"

# include js, css files in header of web template
# web_include_css = "/assets/multibranch/css/multibranch.css"
# web_include_js = "/assets/multibranch/js/multibranch.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "multibranch/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Invoice" : "public/js/sales_invoice.js",
              "Sales Order" : "public/js/sales_order.js",
              "Purchase Invoice" : "public/js/purchase_invoice.js",
              "Purchase Order" : "public/js/purchase_order.js",
              "Stock Entry" : "public/js/stock_entry.js",
              "Material Request" : "public/js/material_request.js",
              "Delivery Note" : "public/js/delivery_note.js",}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "multibranch/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "multibranch.utils.jinja_methods",
# 	"filters": "multibranch.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "multibranch.install.before_install"
# after_install = "multibranch.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "multibranch.uninstall.before_uninstall"
# after_uninstall = "multibranch.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "multibranch.utils.before_app_install"
# after_app_install = "multibranch.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "multibranch.utils.before_app_uninstall"
# after_app_uninstall = "multibranch.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "multibranch.notifications.get_notification_config"

# Permissions
# -----------js
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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"multibranch.tasks.all"
# 	],
# 	"daily": [
# 		"multibranch.tasks.daily"
# 	],
# 	"hourly": [
# 		"multibranch.tasks.hourly"
# 	],
# 	"weekly": [
# 		"multibranch.tasks.weekly"
# 	],
# 	"monthly": [
# 		"multibranch.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "multibranch.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "multibranch.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "multibranch.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["multibranch.utils.before_request"]
# after_request = ["multibranch.utils.after_request"]

# Job Events
# ----------
# before_job = ["multibranch.utils.before_job"]
# after_job = ["multibranch.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"multibranch.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }



fixtures = [{
    "dt":"Custom Field",
    "filters":[
        ["name","in",[
            "Material Request-custom_pos_profile",
            "Delivery Trip-custom_pos_profile",
            "Delivery Note-custom_pos_profile",
            "Stock Entry-custom_pos_profile",
            "Quotation-custom_pos_profile",
            "Sales Order-custom_pos_profile",
            "Supplier Quotation-custom_pos_profile",
            "Purchase Receipt-custom_pos_profile",
            "Purchase Invoice-custom_pos_profile",
            "Purchase Order-custom_pos_profile",

           
        ]]
    ]
},
{
    "dt":"Property Setter",
    "filters":[
        ["name","in",[
            "Sales Invoice-pos_profile-depends_on",
           


            ]
         ]
    ]

},
]
