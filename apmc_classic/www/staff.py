import frappe

def get_context(context):

    context.staff_list = frappe.get_all(
        "Staff Details",
        fields=[
            "employee_name",
            "designation",
            "mobile",
            "photo",
            "email",
            "joining_date"
        ]
    )

    return context