import frappe
from frappe.utils import today

def get_context(context):

    # Gallery Data
    context.gallery = frappe.get_all(
        "Gallery",
        fields=["image"]
    )

    # Market Rates Data
    context.market_rates = frappe.get_all(
        "Market Rates",
        filters={
            "rate_date": today()
        },
        fields=[
            "product_name",
            "avg_price",
            "min_price", 
            "max_price"
        ]
    )

    context.today_date = today()

    # Notice Tender Data
    context.notices = frappe.get_all(
        "Notice Tender",
        fields=["title"],
        order_by="creation desc"
    )
