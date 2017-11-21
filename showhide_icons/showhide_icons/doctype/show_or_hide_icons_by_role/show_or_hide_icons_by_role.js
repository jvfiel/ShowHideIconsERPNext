frappe.ui.form.on('Show or Hide Icons by Role', {
	refresh: function(frm) {

	},

});

frappe.ui.form.on('Show or Hide Icons by Role',"onload",function (frm) {
	frappe.call({
		//showhide_icons.showhide_icons.doctype.show_or_hide_icons_by_role.show_or_hide_icons_by_role.
			method: "showhide_icons.showhide_icons.doctype.show_or_hide_icons_by_role.show_or_hide_icons_by_role.get_icons",
			args: {
			},
			callback: function (r) {
				// console.log(r.message);
				// console.log(frm);
				// frm.doc.set_df_property('modules','icon', 'options', r.message);
				// frm.refresh_field('modules');

				//frappe.meta.get_docfield(“TABLE Doctype NAME”,“FIELDNAME”, cur_frm.doc.name);
				var df = frappe.meta.get_docfield('Show Hide Desktop Icons','icon', cur_frm.doc.name);
				// console.log(df);
				df.options = r.message;
				frm.refresh_field('modules');
			}
		});
}
);
