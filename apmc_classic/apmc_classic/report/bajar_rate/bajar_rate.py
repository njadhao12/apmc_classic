# Copyright (c) 2026, Yes and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": "Product Name",
            "fieldname": "product_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Min Price",
            "fieldname": "min_price",
            "fieldtype": "Float",
            "width": 120
        },
        {
            "label": "Max Price",
            "fieldname": "max_price",
            "fieldtype": "Float",
            "width": 120
        },
        {
            "label": "Avg Price",
            "fieldname": "avg_price",
            "fieldtype": "Float",
            "width": 120
        },
        {
            "label": "Rate Date",
            "fieldname": "rate_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "Quantity",
            "fieldname": "quantity",
            "fieldtype": "Float",
            "width": 120
        },
        {
            "label": "Unit",
            "fieldname": "unit",
            "fieldtype": "Data",
            "width": 100
        }
    ]


def get_data(filters):
    conditions = []

    if filters.get("product_name"):
        conditions.append("product_name = %(product_name)s")

    if filters.get("unit"):
        conditions.append("unit = %(unit)s")

    if filters.get("from_date"):
        conditions.append("rate_date >= %(from_date)s")

    if filters.get("to_date"):
        conditions.append("rate_date <= %(to_date)s")

    where_clause = " AND ".join(conditions)
    if where_clause:
        where_clause = "WHERE " + where_clause
    else:
        where_clause = "WHERE 1=1"

    return frappe.db.sql(f"""
        SELECT
            product_name,
            min_price,
            max_price,
            avg_price,
            rate_date,
            quantity,
            unit
        FROM `tabMarket Rates`
        {where_clause}
        ORDER BY rate_date DESC
    """, filters, as_dict=True)