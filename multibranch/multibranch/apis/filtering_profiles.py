import frappe
from erpnext.stock.get_item_details import get_pos_profile

@frappe.whitelist()
def set_pos_profile(company):
    pos_profile = get_pos_profile(company) or {}
    
    if not pos_profile:
        return
    return pos_profile.get('name')

@frappe.whitelist()
def get_pos_cost_center(pos=None):
	if pos:
		return frappe.db.get_value("POS Profile", pos, ["cost_center"])