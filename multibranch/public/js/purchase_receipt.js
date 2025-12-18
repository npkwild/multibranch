frappe.ui.form.on('Purchase Receipt', {
    onload:function(frm){
        if (frm.doc.company && !frm.doc.pos_profile) {
            frappe.call({
                method: "multibranch.multibranch.apis.filtering_profiles.set_pos_profile",
                args: {
                    company: frm.doc.company,
                },
                callback: function(r) {
                    if (!r.exc) {
                        if (r.message) {
                            frm.set_value("pos_profile", r.message);
                            frappe.call({
                                    method:"multibranch.multibranch.apis.filtering_profiles.get_pos_cost_center",
                                args:{pos:r.message},
                                callback:function(c){
                                    if(c.message){
                                        frm.set_value('cost_center', c.message);
                                        frm.doc.items.forEach(item =>{
                                            frappe.model.set_value(item.doctype, item.name, 'cost_center', c.message);
                                        });
                                        frm.refresh_field('items');
                                    }
                                }
                            });
                        }
                    }
                }
            });
        } else if (!frm.doc.company) {
            frappe.msgprint(__("Please specify Company to proceed"));
        }
    },
})
frappe.ui.form.on('Purchase Receipt Item', {
    item_code:function(frm, cdt, cdn){
        let row = locals[cdt][cdn];
        if(frm.doc.pos_profile && row.item_code){
            frappe.call({
                method:"multibranch.multibranch.apis.filtering_profiles.get_pos_cost_center",
                args:{pos:frm.doc.pos_profile},
                callback:function(c){
                    if(c.message){
                        frappe.model.set_value(cdt, cdn, 'cost_center', c.message);
                        frm.refresh_field('items');
                    }
                }
            });
        }
    }
})
