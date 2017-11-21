# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "showhide_icons"
app_title = "Showhide Icons"
app_publisher = "johnf@bl3ndlabs.com"
app_description = "Showhide Icons"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "johnf@blendlabs.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/showhide_icons/css/showhide_icons.css"
# app_include_js = "/assets/showhide_icons/js/showhide_icons.js"

# include js, css files in header of web template
# web_include_css = "/assets/showhide_icons/css/showhide_icons.css"
# web_include_js = "/assets/showhide_icons/js/showhide_icons.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Website user home page (by function)
# get_website_user_home_page = "showhide_icons.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "showhide_icons.install.before_install"
# after_install = "showhide_icons.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "showhide_icons.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"showhide_icons.tasks.all"
# 	],
# 	"daily": [
# 		"showhide_icons.tasks.daily"
# 	],
# 	"hourly": [
# 		"showhide_icons.tasks.hourly"
# 	],
# 	"weekly": [
# 		"showhide_icons.tasks.weekly"
# 	]
# 	"monthly": [
# 		"showhide_icons.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "showhide_icons.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "showhide_icons.event.get_events"
# }

