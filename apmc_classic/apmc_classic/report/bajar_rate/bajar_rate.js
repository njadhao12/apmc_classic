// Copyright (c) 2026, Yes and contributors
// For license information, please see license.txt

frappe.query_reports["Bajar Rate"] = {
    "filters": [
        {
            fieldname: "product_name",
            label: "Product Name",
            fieldtype: "Data"
        },
        {
            fieldname: "from_date",
            label: "From Date",
            fieldtype: "Date"
        },
        {
            fieldname: "to_date",
            label: "To Date",
            fieldtype: "Date"
        },
        {
            fieldname: "unit",
            label: "Unit",
            fieldtype: "Data"
        }
    ]
};