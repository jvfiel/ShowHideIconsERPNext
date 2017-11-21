# -*- coding: utf-8 -*-
# Copyright (c) 2015, Chris Ian Fiel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.desk.doctype.desktop_icon.desktop_icon import clear_desktop_icons_cache
from frappe.core.page.modules_setup.modules_setup import set_hidden_list
from frappe.desk.doctype.desktop_icon.desktop_icon import get_all_icons

#bench execute wela.school_setup.doctype.show_or_hide_icons_by_role.show_or_hide_icons_by_role.get_user_icon_dict
def get_user_icon_dict():
    desktop_icon = ""
    desktop_icon = "00013bb644"
    icon_doc = frappe.get_doc("Desktop Icon", desktop_icon)
    dict = icon_doc.as_dict()
    print dict

    # {
    #     u'doctype': u'Desktop Icon',
    #     u'owner': u'stufipylol@live.com',
    #     u'label': u'KHS Mastersheets',
    #     u'blocked': 0,
    #     u'hidden': 0,
    #     u'type': u'module',
    #     u'name': u'00013bb644',
    #     u'idx': 11,
    #     u'module_name': u'KHS Mastersheets',
    # }

@frappe.whitelist()
def get_icons():
    print "=============GET ICONS============="
    icons = []
    for icon in frappe.db.sql("""SELECT DISTINCT module_name FROM `tabDesktop Icon`"""):
        icons.append(icon[0])
    print icons
    return icons

class ShoworHideIconsbyRole(Document):

    def validate(self):
        #first get the users of that role


        icons = []
        icons_list = []

        if self.specific_user:
            user_sql = """ parent='{0}'""".format(self.specific_user)
            master_sql = """SELECT parent FROM `tabHas Role` WHERE {0} and parenttype='User'""".format(user_sql)
        else:
            # user_sql = ""
            master_sql = """SELECT parent FROM `tabHas Role` WHERE role='{0}' and parenttype='User'""".format(self.role)

        for module in self.modules:
            icons.append({'module_name':module.icon,'idx':module.idx})

        for module in self.modules:
            icons_list.append(str(module.icon))

        print icons
        print icons_list

        # master_sql = """SELECT parent FROM `tabUserRole` WHERE role='{0}' {1}""".format(self.role,user_sql)

        master_db = frappe.db.sql(master_sql,as_dict=True)

        print master_sql
        print master_db

        for user in master_db:
            print "======================OWNER=============================="
            print user
            if user['parent'] == "Administrator":
                print "======================SKIP OWNER========================="
                continue

            if icons_list:
                icons_list = str(icons_list).replace('[','(')
                icons_list = icons_list.replace(']',')')
            #
            # #hide the rest
            #
            hidden_sql = """SELECT DISTINCT module_name FROM `tabDesktop Icon` WHERE standard=1 AND module_name NOT IN {0}"""\
                .format(icons_list)


            exclude_list = ['Issue Ticket','Quality Tracking']
            # print hidden_sql
            hidden_icons = frappe.db.sql(hidden_sql)
            # print hidden_icons
            hidden_list = []
            if hidden_icons:
                for icon in hidden_icons:
                    if str(icon[0]) not in exclude_list:
                        # print icon
                        hidden_list.append(str(icon[0]))
            print hidden_list
            set_hidden_list(hidden_list,user['parent'])


            print "======================END OWNER=========================="
        frappe.db.commit()
        # clear_desktop_icons_cache()