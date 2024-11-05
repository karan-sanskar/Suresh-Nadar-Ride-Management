# Copyright (c) 2024, suresh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		table_total = 0
		for i in self.services:
			table_total += i.get('currency')
		self.total_amount  = self.price_per_km * self.estimated_km + table_total
